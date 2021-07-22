from unittest import mock

import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
)

from ..core.main import get_application
from .utils import TestModel, HEADERS


@pytest.mark.asyncio
@mock.patch("lib.tests.utils.TestModel")
async def test_get_result(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.get("/", headers=HEADERS)

        assert response.status_code == HTTP_200_OK
        assert response.reason_phrase == "OK"
        assert response.num_bytes_downloaded == 148


@pytest.mark.asyncio
@mock.patch("lib.tests.utils.TestModel")
async def test_get_wrong_api_key(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.get("/", headers={"Authorization": "wrong!"})

        assert response.status_code == HTTP_403_FORBIDDEN
        assert response.reason_phrase == "Forbidden"
