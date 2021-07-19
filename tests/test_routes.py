import json
from unittest import mock

import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from ..main import get_application
from ..tests.utils import TestModel, HEADERS, PAYLOAD


@pytest.mark.asyncio
@mock.patch("tests.utils.TestModel")
async def test_post_wrong_api_key(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.post("/", headers={"Authorization": "wrong!"})
    assert response.status_code == HTTP_403_FORBIDDEN
    assert response.reason_phrase == "Forbidden"


@pytest.mark.asyncio
@mock.patch("tests.utils.TestModel")
async def test_model_input(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.post("/", headers=HEADERS, data=json.dumps(PAYLOAD))
    assert response.status_code == HTTP_200_OK
    assert response.json() is None


@pytest.mark.asyncio
@mock.patch("tests.utils.TestModel")
async def test_wrong_model_input(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.post(
            "/", headers=HEADERS, data=json.dumps(["test", "test2"])
        )

        assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY
        assert response.reason_phrase == "Unprocessable Entity"


@pytest.mark.asyncio
@mock.patch("tests.utils.TestModel")
async def test_get_result(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.get("/", headers=HEADERS)

        assert response.status_code == HTTP_200_OK
        assert response.reason_phrase == "OK"
        assert response.num_bytes_downloaded == 148


@pytest.mark.asyncio
@mock.patch("tests.utils.TestModel")
async def test_get_wrong_api_key(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.get("/", headers={"Authorization": "wrong!"})

        assert response.status_code == HTTP_403_FORBIDDEN
        assert response.reason_phrase == "Forbidden"
