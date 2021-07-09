from collections import Callable
from typing import Any

from core.model_base import PredictionModelBase


class PredictionModelFactory:
    """The factory class for creating Prediction Models"""

    registry: Any
    """ Internal registry for available models """

    @classmethod
    def register(cls) -> Callable:
        """Class method to register prediction model class and creates a instance to the internal registry.
        Returns:
            The Executor class itself.
        """

        def inner_wrapper(wrapped_class: PredictionModelBase) -> Callable:
            cls.registry = wrapped_class()
            return wrapped_class

        return inner_wrapper

    @classmethod
    def get_executor(cls) -> "PredictionModelBase":
        """get command to get the Prediction Model Instance.
        This method gets the appropriate Prediction model class from the registry.
        Returns:
            Instance of the prediction model is passed.
        """
        return cls.registry
