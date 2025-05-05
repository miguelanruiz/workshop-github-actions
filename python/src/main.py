from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from configs.config_version import __version__
from pathlib import Path
from routers import (
    router_github,
    router_health,
)
import json

CURRENT_PATH = Path(__file__).resolve().parent

description = open(f"{CURRENT_PATH}/docs/documentation.md", "r")
tags_metadata = open(f"{CURRENT_PATH}/docs/metadata.json", "r")

app = FastAPI(
    title="FastAPI Containerized Build Deploy Example",
    description=description.read(),
    contact={"name": "DevTools"},
    version=__version__,
    docs_url="/docs",
    redoc_url=None,
    servers=[{"url": "/", "description": "Root URL"}],
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    openapi_tags=json.load(tags_metadata),
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_github.router, tags=["GitHub"])
app.include_router(router_health.router, tags=["Health"])


@app.get(
    path="/",
    response_class=RedirectResponse,
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    include_in_schema=False,
)
async def redirect_to_docs():
    response = RedirectResponse(url="/docs")
    return response
