from typing import Dict

from lib.core import PredictionModelBase

HEADERS = {"Authorization": "secret"}
PAYLOAD = {
    "Clinical_T": "cT1",
    "Clinical_N": "cN0",
}


class TestModel(PredictionModelBase):
    def run_calculation(self, model_input: Dict[str, str]):
        raise NotImplementedError

    def static_template_result(self):
        pass

    def initial_start_event(self):
        raise NotImplementedError
