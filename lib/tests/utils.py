from typing import Dict

from ..core import PredictionModelBase

PAYLOAD = {
    "Clinical_T": "cT1",
    "Clinical_N": "cN0",
}


class TestModel(PredictionModelBase):
    def run_calculation(self, model_input: Dict[str, str]):
        pass

    def static_template_result(self):
        return self

    def initial_start_event(self):
        pass
