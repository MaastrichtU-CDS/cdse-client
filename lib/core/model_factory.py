from abc import ABC


def singleton(real_cls):
    class SingletonFactory(ABC):
        instance = None

        def __new__(cls, *args, **kwargs):
            if not cls.instance:
                cls.instance = real_cls(*args, **kwargs)
            return cls.instance

    SingletonFactory.register(real_cls)
    return SingletonFactory


@singleton
class PredictionModelStore:
    used_model = None

    def __init__(self, prediction_model):
        self.used_model = prediction_model

    def get_model_instance(self):
        return self.used_model
