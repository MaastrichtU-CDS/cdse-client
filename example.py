from typing import Dict

import main
from core.model_base import PredictionModelBase
from core.model_factory import PredictionModelFactory


@PredictionModelFactory.register()
class MyExampleModel(PredictionModelBase):
    def run_calculation(self, model_input: Dict[str, str]):
        self.return_result(model_input)
        pass

    def return_result(self, calculation_results: Dict[str, str]):
        super().return_result(calculation_results)
        pass


if __name__ == "__main__":
    main.run()
