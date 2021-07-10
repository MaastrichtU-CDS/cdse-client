from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

config = Config(".env")

PORT: int = config("PORT", cast=int, default=1312)
INVOCATION_HOST: str = config("INVOCATION_HOST", default="http://localhost:8000/api/v1")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_TOKEN: Secret = config("SECRET_TOKEN", cast=Secret)
PROJECT_NAME: str = config("PROJECT_NAME", default="CDSE - CLient")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
