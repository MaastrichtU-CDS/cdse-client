import json

import responses
from ..services.client import Client


@responses.activate
def test_client_ready():
    responses.add(
        responses.GET,
        "http://localhost:8000/api/v1/ready",
        status=200,
    )

    Client().get_ready()
    assert len(responses.calls) == 1


@responses.activate
def test_client_result():
    test_payload = {"test": "x"}
    responses.add(
        responses.POST,
        "http://localhost:8000/api/v1/result",
        status=200,
    )

    Client().post_result(test_payload)
    assert len(responses.calls) == 1
    assert test_payload == json.loads(responses.calls[0].request.body)
