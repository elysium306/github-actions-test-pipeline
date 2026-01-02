# GitHub Actions Test Pipeline

## Purpose

Demonstrates a CI/CD pipeline using GitHub Actions to run automated tests on
every push and pull request.

## Pipeline Flow

-   Triggered on push and pull request
-   Install dependencies
-   Execute automated tests
-   Fail build on test errors

## Tech Stack

-   GitHub Actions
-   YAML
-   Python / Playwright (test runner)

## Key Concepts Demonstrated

-   CI/CD automation
-   Pipeline-as-code
-   Fast feedback on code changes

## Status

Initial pipeline setup. Additional optimizations planned.

## Roadmap

-   [ ] Add matrix builds
-   [ ] Add test reports
-   [ ] Integrate Docker runner

## How it works

This repo demonstrates a minimal CI pipeline using GitHub Actions that runs automated tests on every push and pull request.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```
