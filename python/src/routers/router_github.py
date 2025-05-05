from configs.config_limiter import limiter
from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

router = APIRouter()


@router.get(
    path="/github-status",
    description="Get the GitHub status",
    name="github-status",
    include_in_schema=True,
)
@limiter.limit("5/second")
def get_github_status(
    request: Request,
) -> JSONResponse:
    """
    Endpoint to get the GitHub status.
    """
    headers = {
        "Accept": "application/json",
    }
    try:
        response = requests.get(
            url="https://www.githubstatus.com/api/v2/status.json",
            headers=headers,
            verify=False,
        )
        if response.ok:
            return JSONResponse(
                content=jsonable_encoder(response.json()),
                media_type="application/json",
                status_code=response.status_code,
            )
        else:
            return JSONResponse(
                content=jsonable_encoder(
                    {
                        "message": "Failed to get GitHub status",
                        "details": response.text,
                    }
                ),
                media_type="application/json",
                status_code=response.status_code,
            )
    except requests.exceptions.RequestException as error:
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "message": "Failed to get GitHub status",
                    "details": str(error.args[0]),
                }
            ),
            media_type="application/json",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
