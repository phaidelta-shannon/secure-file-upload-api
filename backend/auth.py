from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEY = "mysecureapikey"
API_KEY_NAME = "api_key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key