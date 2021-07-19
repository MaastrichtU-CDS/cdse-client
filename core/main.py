import os

import uvicorn
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .http_errors import http_error_handler

from api.routes import router as api_router
from .config import ALLOWED_HOSTS, DEBUG, PROJECT_NAME, PORT, STATIC_DIR
from services.events import create_start_app_handler
from .model_factory import PredictionModelStore


def get_application(prediction_model, optional_extra_routes) -> FastAPI:
    PredictionModelStore(prediction_model())

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG)

    if os.path.isdir("static"):
        application.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)

    application.include_router(api_router)

    if optional_extra_routes is not None:
        application.include_router(optional_extra_routes)

    return application


def run(prediction_model, optional_extra_routes=None):
    app = get_application(prediction_model, optional_extra_routes)
    uvicorn.run(app, host="0.0.0.0", port=PORT)
