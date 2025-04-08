# 🛰️ TrackSensei Telemetry 🛰️

This is the **on-device data collection module** for the TrackSensei system.
It runs on a Jetson Nano and records real-time telemetry using GPS and sensor data during racing sessions. The data is later uploaded to the TrackSensei server for analysis and feedback.

---

## 🚀 Setup

### 1. Clone the repository and install dependencies with Poetry

```bash
git clone https://github.com/rudysuarez1/TrackSensei-Telemetry.git
cd TrackSensei-Telemetry
```

### Running on macOS:
```bash
brew install python

# Intel Macs:
curl -sSL https://install.python-poetry.org | /usr/local/bin/python3

# Apple Silicon (M1/M2):
curl -sSL https://install.python-poetry.org | /opt/homebrew/bin/python3
```

Then install project dependencies:
```bash
poetry install
```

---

### 2. Environment Configuration

Create a `.env` file from the example:
```bash
cp .env.example .env
```

Update your `.env` file to match your Jetson Nano setup:
```env
GPS_PORT=/dev/ttyTHS1
```

---

## ✅ Pre-commit and Code Quality

Install pre-commit hooks:

```bash
poetry run pre-commit install
```

To run all code quality checks manually:

```bash
poetry run pre-commit run --all-files
poetry run pyright
poetry run pytest
poetry run pytest --cov
```

Or all together:

```bash
poetry run pre-commit run --all-files && poetry run pyright && poetry run pytest
```

---

## 🧪 Running Tests

```bash
poetry run pytest
poetry run pytest --cov
```

---

## 🧪 First-Time Dev Quickstart

```bash
poetry shell
poetry run python -m app
```

This runs the telemetry app and starts logging GPS data from your configured device.

---

## 💧 Tech Stack

- Python 3.10+
- Poetry
- Pyright
- Pre-commit
- Pytest
- pynmea2
- python-dotenv
