from fastapi import HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from ..core.config import SECRET_TOKEN

api_token_header = APIKeyHeader(name="Authorization", auto_error=False)


async def check_session_token(session_token):

    if session_token == str(SECRET_TOKEN):
        pass
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="No valid API key")
