from typing import Dict

from ..core import PredictionModelBase

PAYLOAD = {
    "Clinical_T": "cT1",
    "Clinical_N": "cN0",
}


class TestModel(PredictionModelBase):
    @staticmethod
    def run_calculation(model_input: Dict[str, str]):
        pass

    @staticmethod
    def static_template_result():
        pass

    @staticmethod
    def initial_start_event():
        pass
