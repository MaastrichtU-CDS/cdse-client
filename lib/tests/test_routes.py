from unittest import mock

import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_403_FORBIDDEN,
)

from ..core.main import get_application
from .utils import TestModel


@pytest.mark.asyncio
@mock.patch("lib.tests.utils.TestModel")
async def test_get_wrong_api_key(model_mock: TestModel):
    async with AsyncClient(
        app=get_application(model_mock, None), base_url="http://test"
    ) as ac:
        response = await ac.get("/?session_token=wrong")

        assert response.status_code == HTTP_403_FORBIDDEN
        assert response.reason_phrase == "Forbidden"
