# Workshop - GitHub Actions

:rocket: A repository focused on exploring GitHub Actions as a powerful CI/CD automation tool.

## Agenda

- About GitHub Actions
- Pricing
  - Options
  - About Self-Hosted Runners
  - About GitHub Hosted Runners
- Who use GitHub Actions?
- Demo pt. 1
  - Setup an example Python project
  - Let's allow actions to be executed in the repository
  - Create the secrets
  - Steps:
    - Checkout Code
    - Setup Python
    - Install Dependencies
    - Run Lint
    - Run Tests
    - Run Build
    - Upload Package to the GitHub Run
    - Publish Package to PyPi
- How to set up a local Runner for testing?
- Demo pt. 2
  - Jobs in Parallel
  - Jobs in Sequence
  - Steps:
    - Docker Login
    - Add the Container Metadata
    - Setup Docker QEMU
    - Setup Docker Buildx
    - Build and Push
- Demo pt. 3
  - Trigger a Workflow when a Pull Request is merged
  - Create a Release in the repository when the Pull Request is merged

## Workshop Content

Each of the Workshop sections is described in the following table.

| **`#`** | **Section**                                                                  |
| ------- | ---------------------------------------------------------------------------- |
|    1    | [Introduction](./docs/workshop/0-introduction.md)                            |
|    2    | [Prerequisites to Develop the Workshop](./docs/workshop/1-prerequisites.md)  |
|    3    | [Deploy a Python Package](./docs/workshop/2-setup-example-project.md)        |
|    4    | [Set the Secrets and Variables](./docs/workshop/3-secrets-and-variables.md)  |
|    5    | [Deploy a Docker Container](./docs/workshop/4-dockerized-example-project.md) |

## FAQ

1. Are there any examples of workflows anywhere?
2. The best place to learn?
3. When do I know an error is due to my Workflow configuration and not GitHub services?
4. How many jobs can I run in parallel?
5. How many reusable workflows can I use?
6. What is the maximum time a job can be in running state?
7. Are secrets really secret/secure?
8. What about the CD?

## Roadmap

- Add a section for [_Concurrency_](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs)
- Add a section to create, edit, or delete issues or pull requests using the `github-actions[bot]`
- Add a section to explore the avaiable GitHub Actions metrics in the UI
- Add a section with some points to do Workflow management
- Add a section to explain how to [cache dependencies](https://github.com/actions/cache) in Python and improve the total execution time of a workflow
- Add a section of how to configure and run the [Dependabot](https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide)
