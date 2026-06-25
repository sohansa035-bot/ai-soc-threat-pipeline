# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Modular architecture (`api`, `classifier`, `parser`, `models`, `dashboard`)
- FastAPI backend for log analysis and playbook generation
- Streamlit frontend integration with the REST API
- Initial suite of sample logs (`failed_login.log`, `sql_injection.log`, `ddos.log`)
- Pytest framework with basic test coverage
- GitHub Actions workflows for continuous integration (Lint & Test)
- Professional documentation suite (`CONTRIBUTING.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`)

## [1.0.0] - 2026-06-25

### Added
- Initial release of the Autonomous AI Security Operations Dashboard
- Streamlit-based monolithic prototype
- Basic Python heuristic log parser
- Dockerfile and docker-compose deployment files
