<div align="center">

# Abalone Project

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: flake8](https://img.shields.io/badge/linting-flake8-yellowgreen.svg)](https://flake8.pycqa.org/)

</div>

## Context of the project

### Description

**Objective**: predict the age of abalone (Rings + 1.5) from various physical measurements and industrialise the machine learning workflow.

**Dataset**: The dataset can be downloaded at [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset).

**Authors**: [Eva Toledano](https://github.com/eva-toledano), [Qiling Zhu](https://github.com/qly0923), [Khushi Verma](https://github.com/khushiverma12
), [Elise Barattini](https://github.com/ebarattini), [Tanmay Kale](https://github.com/Cubestormer-IV)

## 1. Setup
### Setup the Virtual Environment

**Option 1: Conda**

Create and activate the environment:
```bash
conda env create --file environment.yml
conda activate <envname>
```
TODO - replace envname

**Option 2: Pip and Virtualenv**

Create and activate the environment:
```bash
python3 -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
.\venv\Scripts\activate
```

### Install the Dependencies

Install the requirements:
```bash
pip install -r requirements.txt # Install the main dependencies for the project
pip install -r requirements-dev.txt # Install development tools such as flake8, black

```


## 2. Running the code
### Running the Prefect Worklow
Configure the Prefect API URL:
```bash
prefect config set PREFECT_API_URL=TODO
```

Verify SQLite Installation (used as the Prefect backend database):
```bash
sqlite3 --version
```

Start the Prefect Server:
```bash
prefect server start --host 0.0.0.0
```

Run the Model Training Workflow:
```bash
python src/modelling/main.py
```

Access the Prefect UI:
TODO-paste url


### Deploying the API
TODO
