# Paved Road Testing: Poetry Python Example

This is an application example for testing.

## Table of Contents

- [Paved Road Testing: Poetry Python Example](#paved-road-testing-poetry-python-example)
  - [Table of Contents](#table-of-contents)
  - [Configuring Your Project](#configuring-your-project)
  - [Legal](#legal)

## Configuring Your Project

This example project was created using `poetry` for dependency management, and [FastAPI](https://fastapi.tiangolo.com/) as framework. We strongly recommend that you follow our directory structure example.

- See the conventions outlined in the Python Packaging Authority's Documentation on [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/).
- For more information on `poetry`, see the introduction section of their [documentation](https://python-poetry.org/docs/).
- Try to follow the file structure for [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) in [FastAPI](https://fastapi.tiangolo.com/).

## Legal

We have used the open source framework [FastAPI](https://fastapi.tiangolo.com/), with the [MIT License](https://github.com/fastapi/fastapi?tab=MIT-1-ov-file#readme) to implement this project for testing. The project has two endpoints.

- GitHub health, to check the status of the GitHub components. Check the docs [here](https://www.githubstatus.com/api). Example of the response below.

```json
{
  "page": {
    "id": "kctbh9vrtdwd",
    "name": "GitHub",
    "url": "https://www.githubstatus.com",
    "time_zone": "Etc/UTC",
    "updated_at": "2024-09-06T07:43:58.589Z"
  },
  "status": {
    "indicator": "none",
    "description": "All Systems Operational"
  }
}
```

- Local health, to return a response on the resource status and general information of the system that call the endpoint. Example of the response below.

```json
{
  "system": "Darwin",
  "processor": "arm",
  "architecture": [
    "64bit",
    ""
  ],
  "release": "23.6.0",
  "version": "Darwin Kernel Version 23.6.0: Mon Jul 29 21:16:46 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T8112",
  "machine": "arm64",
  "memory": {
    "total": 17179869184,
    "available": 3018440704,
    "percent": 82.4,
    "used": 5404819456,
    "free": 98189312,
    "active": 2925805568,
    "inactive": 2840117248,
    "wired": 2479013888
  },
  "cpu": 37.2,
  "disk": {
    "total": 494384795648,
    "used": 10262859776,
    "free": 375962390528,
    "percent": 2.7
  }
}
```
