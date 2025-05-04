from configs.config_limiter import limiter
from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import platform
import psutil

router = APIRouter()


@router.get(
    path="/health",
    description="Get the health of the client",
    name="health",
    include_in_schema=True,
)
@limiter.limit("5/second")
def get_github_status(
    request: Request,
) -> JSONResponse:
    """
    Endpoint to get the health of the client.
    """
    try:
        system_info = {
            "system": platform.system(),
            "processor": platform.processor(),
            "architecture": platform.architecture(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "memory": psutil.virtual_memory()._asdict(),
            "cpu": psutil.cpu_percent(interval=1),
            "disk": psutil.disk_usage("/")._asdict(),
        }
        return JSONResponse(
            content=jsonable_encoder(system_info),
            media_type="application/json",
            status_code=status.HTTP_200_OK,
        )
    except Exception as error:
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "message": "Failed to get health status",
                    "details": str(error),
                }
            ),
            media_type="application/json",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
