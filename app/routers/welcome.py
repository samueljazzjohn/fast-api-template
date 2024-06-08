from os import environ
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.helpers.decorators import handleAPIError


if environ.get('DEBUG'):
    import debugpy
    debugpy.listen(5678)
    debugpy.wait_for_client()

router = APIRouter()


@router.get("/")
@handleAPIError
async def welcome():
    try: 
        return JSONResponse(status_code=200, content={"Status": True, "message": "Welcome"})
    except Exception as e:
        error_message = "Failed to connect" + str(e)
        return JSONResponse(status_code=501, content={"Status": False, "message": error_message})
    
