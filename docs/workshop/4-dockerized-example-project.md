# Dockerize the Python Project


## Manual Procedure

> ![CAUTION]
> Because we are using [`chainguard`](https://images.chainguard.dev/directory/image/python/versions), this version should be the latest minor version of Python. At the time of writing the workflow, the version is 3.13.

To Dockerize the example project, you should be aware of what is happening in the [`Dockerfile`](../../python/Dockerfile). Some characteristics of the `Dockerfile`.

- It's a multi-stage build, so there's a `dev` image where the application is built, and a final image where the application runs.
- There's an `ARG` called `PYTHON_VERSION` in case the Python version changes for the images used.
- The registry, name, and version are chosen when running the `docker build` command.

Set the credentials

```bash
export DOCKER_HUB_USERNAME=caprivm
export DOCKER_HUB_TOKEN=
```

Login to the registry

```bash
docker login hub.docker.com -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_TOKEN
```

Build the container

```bash
docker build \
--build-arg PYTHON_VERSION=3.13 \
--tag fastapi-poetry-deploy-example:latest \
-f python/. .
```

Run the container locally

```bash
docker run -d -p 8000:8000 \
--name fastapi-poetry-deploy-example \
fastapi-poetry-deploy-example:latest
```

Check if the application is running in `http://localhost:8000`. You should see a result similar to [this section](./2-setup-example-project.md#execute-the-application).

## Exercise in GitHub Actions

The exercise consists of following the steps defined in the diagram until producing a Docker container.

### Actions Catalog

In this section you will find a catalog of actions to use in implementing the suggested workflow.

| **Action**           | **Source**                                                        |
| -------------------- | ----------------------------------------------------------------- |
| Checkout             | [`actions/checkout`](https://github.com/actions/checkout)         |
| Docker Login         | [`docker/login-action`](https://github.com/docker/login-action)   |
| Docker Metadata      | [`docker/metadata-action`](https://github.com/docker/metadata-action)  |
| Setup QEMU           | [`setup-qemu-action`](https://github.com/docker/setup-qemu-action)     |
| Setup `buildx`       | [`setup-buildx-action`](https://github.com/docker/setup-buildx-action) |
| Build and Push       | [`build-push-action`](https://github.com/docker/build-push-action)     |
