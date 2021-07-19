# from main import run
# from typing import Dict, Union
# from fastapi import APIRouter
#
# from core.model_base import PredictionModelBase
#
# router = APIRouter()
#
#
# class MyExampleModel(PredictionModelBase):
#     result = []
#     def initial_start_event(self):
#         print("run before server started, so you can do pre calculations")
#         pass
#
#     def run_calculation(self, model_input: Dict[str, Union[str, int]]):
#         self.post_result(model_input)
#         pass
#
#     def static_template_result(self):
#         print("run when server request static template files")
#         pass
#
#
# @router.get("/_query")
# def example_extra_route():
#     print("example route")
#
#
# if __name__ == "__main__":
#     run(MyExampleModel, router)
