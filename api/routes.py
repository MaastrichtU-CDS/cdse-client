from typing import Dict
from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from uvicorn.middleware.debug import HTMLResponse

from core.model_factory import PredictionModelStore

router = APIRouter()

templates = Jinja2Templates(directory="template")


@router.post("/")
async def post_model_input(model_input: Dict[str, str]):
    PredictionModelStore().get_model_instance().run_calculation(model_input)
    return


@router.get("/", response_class=HTMLResponse)
async def static_result_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "custom": PredictionModelStore()
            .get_model_instance()
            .static_template_result(),
        },
    )
