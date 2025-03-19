# Gandula Rating

A player rating system using VAEP (Valuing Actions by Estimating Probabilities) and the Gandula package, consuming PFF (Pro Football Focus) data.

## Overview

This project implements a player rating system for soccer based on the VAEP framework, which values on-the-ball actions by estimating their impact on the probability of scoring and conceding goals.

## Installation

This project uses `uv` for dependency management. To set up the development environment:

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate a virtual environment
uv venv

# On Windows
.venv\Scripts\activate

# On Unix
source .venv/bin/activate

# Install dependencies
uv pip install -e .
```

## Project Structure

```
gandula-rating/
│
├── data/               # Data files
│   ├── raw/            # Original, immutable data
│   ├── processed/      # Cleaned, transformed data ready for analysis
│   └── interim/        # Intermediate data that has been transformed
│
├── src/                # Source code for use in this project
│   └── gandula_rating/
│       ├── __init__.py
│       ├── data/       # Data loading and processing
│       ├── models/     # ML models and VAEP implementation
│       └── visualization/ # Visualization utilities
│
├── notebooks/          # Jupyter notebooks for exploration and analysis
│
├── config/             # Configuration files
│
├── pyproject.toml      # Project metadata and dependencies
└── README.md           # Project description
```

## Usage

\#TODO

## Data Source

This project uses data from Pro Football Focus (PFF). 

## References

- [VAEP Framework](https://github.com/ML-KULeuven/socceraction)
- [Gandula Package](https://github.com/gandula)

## License

MIT