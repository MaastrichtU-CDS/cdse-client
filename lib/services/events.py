from typing import Callable
from fastapi import FastAPI

from ..core.model_factory import PredictionModelStore
from ..services.client import Client


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        PredictionModelStore().get_model_instance().initial_start_event()

        model_input = Client().get_ready()
        PredictionModelStore().get_model_instance().run_calculation(model_input)

    return start_app
