import main
from typing import Dict
from fastapi import APIRouter

from core.model_base import PredictionModelBase

router = APIRouter()


class MyExampleModel(PredictionModelBase):
    def static_template_result(self):
        pass

    def run_calculation(self, model_input: Dict[str, str]):
        self.post_result(model_input)
        pass


@router.get("/_query")
def example_extra_route():
    print("example route")


if __name__ == "__main__":
    main.run(MyExampleModel, router)
