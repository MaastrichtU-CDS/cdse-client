import threading
from typing import Callable
from fastapi import FastAPI

from services.client import Client


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        def signal_ready():
            Client().post_ready()

        t1 = threading.Thread(target=signal_ready, args=[])
        t1.start()

    return start_app
