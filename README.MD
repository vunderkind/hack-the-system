# Hack the System

Hack the System is a command-line tool that evaluates a candidate’s CV against a job description using a deterministic scoring engine. It produces:
- **Pass Probability (0–100%)** — likelihood of beating an ATS (Applicant Tracking System)
- **Interest Grade (A–F, S)** — qualitative rating of fit and “interestingness”
- **Actionable Recommendations** — targeted suggestions to improve weak areas

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Development](#development)
6. [License](#license)

---

## Features

- Deterministic rule-based scoring
- Configurable weightings for keywords, formatting, and experience
- Exportable JSON or human-friendly console output
- Extensible plugin hooks for custom ATS rules

---

## Prerequisites

- Python ≥ 3.7 (recommended: 3.9–3.13)
- `pip` package installer
- (Optional) Virtual environment tool, e.g. `venv` or `virtualenv`

---

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/your-org/hack-the-system.git
   cd hack-the-system
   ```

2. (Optional) Create & activate a virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install in editable mode (pulls in FastAPI and other dependencies)
   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -e .
   ```

---

## Usage

### Command-line

After installation, you’ll have access to the `hack` command:

```bash
hack --cv path/to/your_CV.pdf \
     --job path/to/job_description.txt \
     --output report.json
```

Common options:

```
--cv      Path to candidate CV (PDF, DOCX, or TXT)
--job     Path to job description (TXT or MD)
--output  Destination file (JSON or CSV). Defaults to stdout.
--format  Output format: json | csv | text (default: text)
--verbose Show detailed scoring breakdown
```

### Python API

You can also import and call the scoring engine directly:

```python
from hacks import app

# Returns a dict with score, grade, and recommendations
result = app.evaluate(cv_path="resume.pdf", job_path="jd.txt")
print(result)
```

---

## Development

1. **Create & activate your virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

3. **Run tests**
   ```bash
   pytest --strict-markers
   ```

4. **Lint & format**
   ```bash
   black .
   flake8
   ```

5. **Start a local server (FastAPI UI)**
   ```bash
   uvicorn hacks.api:app --reload
   ```
   Visit <http://localhost:8000> to experiment with the API frontend.

6. **Building a release**
   ```bash
   python3 -m build
   twine upload dist/*
   ```

---

## License

This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.
