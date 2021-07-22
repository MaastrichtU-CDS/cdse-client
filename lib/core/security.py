import secrets

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from ..core.config import SECRET_TOKEN

api_token_header = APIKeyHeader(name="Authorization", auto_error=False)


async def check_api_token(api_key_header: str = Security(api_token_header)):

    if api_key_header is not None and secrets.compare_digest(
        str(SECRET_TOKEN), api_key_header
    ):
        pass
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="No valid API key")
