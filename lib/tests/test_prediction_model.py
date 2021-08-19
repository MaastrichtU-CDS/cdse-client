from unittest import mock

from fastapi.testclient import TestClient
from ..tests import TestModel
from ..core import PredictionModelStore
from ..core.main import get_application


@mock.patch("lib.services.Client.post_result")
def test_prediction_model_post_result(post_result_mock):
    result = {}
    PredictionModelStore(TestModel)
    TestModel().post_result(result)

    post_result_mock.assert_called_with({"has_result_page": True})


@mock.patch("lib.services.Client.get_ready", return_value=[])
@mock.patch(
    "lib.tests.utils.TestModel.run_calculation",
    side_effect=Exception("Example Error Message"),
)
@mock.patch("lib.services.Client.post_error")
def test_prediction_model_post_error(
    post_error_mock, get_ready_mock, run_calculation_mock
):

    with TestClient(
        app=get_application(TestModel, None), base_url="http://test"
    ) as client:
        post_error_mock.assert_called_with("Example Error Message")
