import os
from abc import abstractmethod, ABC
from typing import Dict

from lib.core.config import TEMPLATE_DIR
from lib.services.client import Client


class PredictionModelBase(ABC):
    @abstractmethod
    def run_calculation(self, model_input: Dict[str, str]):
        """method to get model input and kick off calculations"""
        pass

    @abstractmethod
    def static_template_result(self):
        """method that fills the template index.html file with variables to build a html rendered page"""
        pass

    @abstractmethod
    def initial_start_event(self):
        """method that automatically runs at start-up"""
        pass

    @staticmethod
    def post_result(calculation_results: Dict[str, str]):
        """method to return all calculated results"""
        calculation_results.update({"has_result_page": os.path.isdir(TEMPLATE_DIR)})
        Client().post_result(calculation_results)
        pass
