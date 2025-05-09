## Use the Base Image
FROM cgr.dev/chainguard/python:latest-dev AS dev
USER root

## Create the Application Directory and Virtual Environment
WORKDIR /fastapi-app
RUN python -m venv .venv
RUN source .venv/bin/activate
ENV PATH="/fastapi-app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
RUN pip install poetry tomlkit

## Install the Application Dependencies
COPY . ./
RUN cd python \
    poetry install

## Copy the Application Source Code
FROM cgr.dev/chainguard/python:latest
ARG PYTHON_VERSION=3.13
WORKDIR /fastapi-app
COPY . ./
COPY --from=dev /fastapi-app/.venv /fastapi-app/.venv
ENV PATH="/fastapi-app/.venv/bin:${PATH}" \
    PYTHONPATH="/fastapi-app:/fastapi-app/.venv/lib/python${PYTHON_VERSION}/site-packages:${PATH}" \
    PYTHONUNBUFFERED=1

##
## Run the FastAPI application
EXPOSE 8000
CMD ["/fastapi-app/.venv/bin/fastapi", "run", "python/src/main.py", "--port", "8000", "--host", "0.0.0.0"]
