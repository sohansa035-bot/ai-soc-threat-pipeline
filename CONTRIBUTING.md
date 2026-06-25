# Contributing to AI-SOC Threat Pipeline

First off, thank you for considering contributing to the AI-SOC Threat Pipeline! It's people like you that make open-source such a great community.

## How to Contribute

### 1. Fork and Clone
Fork the repository and clone it locally to your machine.

### 2. Set Up the Environment
Create a virtual environment and install the requirements:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Run Tests
Ensure all tests pass before making your changes:
```bash
pytest tests/
```

### 4. Make Your Changes
Create a new feature branch (`git checkout -b feature/your-feature-name`), make your changes, and write tests for them.

### 5. Submit a Pull Request
Push your branch to your fork and submit a Pull Request against the `main` branch. Ensure your code passes the CI linting and testing workflows.

## Development Guidelines
- Follow PEP 8 style guidelines.
- Ensure all new API endpoints are documented with Pydantic schemas.
- Update the `CHANGELOG.md` with your changes.
