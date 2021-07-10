import os
from abc import abstractmethod, ABC
from typing import Dict

from services.client import Client


class PredictionModelBase(ABC):
    @abstractmethod
    def run_calculation(self, model_input: Dict[str, str]):
        """Abstract method to get model input and kick off calculations"""
        pass

    @abstractmethod
    def static_template_result(self):
        pass

    @staticmethod
    def post_result(calculation_results: Dict[str, str]):
        """method to return all calculation results"""
        calculation_results.update({"has_static_asset": os.path.isdir("../template")})
        Client().post_results(calculation_results)
        pass
