from lib import run, PredictionModelBase, check_session_token
from typing import Dict, Union
from fastapi import APIRouter

router = APIRouter()


class MyExampleModel(PredictionModelBase):
    result = {"x": "y"}

    def initial_start_event(self):
        print("run before server started, so you can do pre calculations")
        pass

    def run_calculation(self, model_input: Dict[str, Union[str, int]]):
        self.post_result(model_input)
        pass

    def static_template_result(self):
        return self


@router.get("/_query")
async def example_extra_route(session_token):
    await check_session_token(session_token)
    print("example route")
    return "ok"

if __name__ == "__main__":
    run(MyExampleModel, router)
