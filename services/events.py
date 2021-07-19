import threading
from typing import Callable
from fastapi import FastAPI

from ..core.model_factory import PredictionModelStore
from ..services.client import Client


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        PredictionModelStore().get_model_instance().initial_start_event()

        def signal_ready():
            Client().get_ready()

        t1 = threading.Thread(target=signal_ready, args=[])
        t1.start()

    return start_app
