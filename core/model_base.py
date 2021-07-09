from abc import ABCMeta, abstractmethod
from typing import Dict

from services.client import Client


class PredictionModelBase(metaclass=ABCMeta):
    """Base class for an executor"""

    def __init__(self, **kwargs):
        """Constructor"""
        pass

    @abstractmethod
    def run_calculation(self, model_input: Dict[str, str]):
        """Abstract method to get model input and kick off calculations"""
        pass

    @abstractmethod
    def return_result(self, calculation_results: Dict[str, str]):
        """Abstract method to return all calculation results"""
        Client().post_results(calculation_results)
        pass
