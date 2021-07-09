from typing import Dict
from fastapi import APIRouter
from core.model_factory import PredictionModelFactory

router = APIRouter()


@router.post("/")
async def post_model_input(model_input: Dict[str, str]):
    PredictionModelFactory.get_executor().run_calculation(model_input)
    return


@router.get("/")
async def get_model_result_assets():
    return "3"
