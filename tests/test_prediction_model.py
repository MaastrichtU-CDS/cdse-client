from unittest import mock

from ..tests.utils import TestModel


@mock.patch("services.client.Client.post_result")
def test_prediction_model_post_result(post_result_mock):
    result = {}
    TestModel().post_result(result)

    post_result_mock.assert_called_with({"has_result_page": True})
