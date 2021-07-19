import os
from fastapi import APIRouter, Request, Depends
from fastapi.openapi.models import APIKey
from starlette.templating import Jinja2Templates
from uvicorn.middleware.debug import HTMLResponse

from core.config import TEMPLATE_DIR
from core.model_factory import PredictionModelStore
from core.security import check_api_token

router = APIRouter()


if os.path.isdir(TEMPLATE_DIR):
    templates = Jinja2Templates(directory=TEMPLATE_DIR)

    @router.get("/", response_class=HTMLResponse)
    async def static_result_page(
        request: Request, api_key: APIKey = Depends(check_api_token)
    ):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "custom": PredictionModelStore()
                .get_model_instance()
                .static_template_result(),
            },
        )
