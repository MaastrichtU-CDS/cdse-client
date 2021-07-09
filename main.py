import uvicorn
from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from api.http_errors import http_error_handler

from api.routes import router as api_router
from core.config import ALLOWED_HOSTS, DEBUG, PROJECT_NAME, PORT
from core.events import create_start_app_handler


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG)

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

    return application


def run():
    app = get_application()
    uvicorn.run(app, host="0.0.0.0", port=PORT)
