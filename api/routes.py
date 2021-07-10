import threading
from typing import Dict
from fastapi import APIRouter, Request, Depends
from fastapi.openapi.models import APIKey
from starlette.templating import Jinja2Templates
from uvicorn.middleware.debug import HTMLResponse

from core.model_factory import PredictionModelStore
from services.security import check_api_token

router = APIRouter()

templates = Jinja2Templates(directory="template")


@router.post("/")
async def post_model_input(
    model_input: Dict[str, str], api_key: APIKey = Depends(check_api_token)
):
    def start_calculation():
        PredictionModelStore().get_model_instance().run_calculation(model_input)

    t2 = threading.Thread(target=start_calculation, args=[])
    t2.start()


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
