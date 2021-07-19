from unittest import mock
from lib.tests import TestModel
from lib.core import PredictionModelStore


@mock.patch("lib.services.Client.post_result")
def test_prediction_model_post_result(post_result_mock):
    result = {}
    PredictionModelStore(TestModel)
    TestModel().post_result(result)

    post_result_mock.assert_called_with({"has_result_page": True})
