# Introduction

This document serves as an introduction to GitHub Actions, a powerful CI/CD platform that enables developers to automate workflows for building, testing, and deploying their applications. It provides an overview of its features, pricing models, and use cases, along with references to additional resources for further exploration.

| **Version Control** | -                          |
| ------------------- | -------------------------- |
| `caprivm`           | <juan.caviedes@neoris.com> |
| Updated             | _May 5, 2025_              |

## Table of Contents

- [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [What is GitHub Actions?](#what-is-github-actions)
  - [Pricing](#pricing)
    - [Self-hosted Runners](#self-hosted-runners)
  - [Who uses GitHub Actions?](#who-uses-github-actions)
  - [References](#references)

## What is GitHub Actions?

_GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production._

> [!IMPORTANT]
> GitHub Actions can help you automate nearly every aspect of your application development processes.

## Pricing

GitHub Actions billing depends on your plan, the use of GitHub-hosted runners, the type of machine, and other factors. Key details are below:

> Let's see the details [here](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions).
>
> - Calculator by GitHub [here](https://github.com/pricing/calculator#actions)

### Self-hosted Runners

A _self-hosted_ runner is a system that you deploy and manage to execute jobs from GitHub Actions on GitHub.

> Let's see the details [here](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners).
>
> - Supported Architectures [here](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/supported-architectures-and-operating-systems-for-self-hosted-runners).
> - Calculator on AWS [here](https://runs-on.com/calculator/).

## Who uses GitHub Actions?

Currently, millions of organizations are registered with GitHub Enterprise.

![Alt text: A visual representation of GitHub Actions customers](../images/introduction-who-use-gha.png)

> Let's see some details [here](https://github.com/customer-stories).
>
> - All the customer stories [here](https://github.com/customer-stories/all).
> - GitHub Blog for CI/CD [here](https://github.blog/enterprise-software/ci-cd/).

## References

| Number | Name                      | Link                                                                                                                                                               |
| ------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | GitHub Actions            | [Understanding GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)                                               |
| 2      | Billing in GitHub Actions | [About Billing in GHA](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions) |
| 3      | _self-hosted_ Runners     | [About _self-hosted_ Runers](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners)                   |
| 4      | Supported Architecture    | [Architectures in _self-hosted_ Runners](https://github.com/pricing/calculator#actions)                                                                            |
| 5      | Calculator on AWS         | [AWS Calculator for GHA](https://runs-on.com/calculator/)                                                                                                          |
| 6      | Calculator by GitHub      | [GitHub Calculator for GHA](https://github.com/pricing/calculator#actions)                                                                                         |
| 7      | CI/CD GitHub Blog         | [GitHub Blog for GHA](https://github.blog/enterprise-software/ci-cd/)                                                                                              |
| 8      | Customer Stories          | [GitHub Customer Stories](https://github.com/customer-stories/all)                                                                                                 |
