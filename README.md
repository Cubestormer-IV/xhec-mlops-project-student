<div align="center">

# Abalone MLOps Project

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: flake8](https://img.shields.io/badge/linting-flake8-yellowgreen.svg)](https://flake8.pycqa.org/)

</div>

## Context of the project

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
conda activate abalone
```

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
To start the Prefect server and enable monitoring:
```bash
prefect server start
```

Set the Prefect API URL to communicate with the server:
```bash
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
```

Verify SQLite Installation (used as the Prefect backend database):
```bash
sqlite3 --version
```

Run a Prefect worker to poll the tasks from the specified work pool:
```bash
prefect worker start --pool "default-agent-pool"
```

To manually start a flow run for an existing deployment:
```bash
prefect deployment run "training-pipeline/My Flow" --param 'data/abalone.csv'
```

To monitor the Prefect dashboard: http://127.0.0.1:4200


### Deploying the API

Build the docker image from the Dockerfile:
```bash
docker build -t abalone-age-prediction -f Dockerfile.app .
```

Run the docker container from the created image:
```bash
docker run -p 8001:8001 abalone-age-prediction
```

To get access to the FastAPI dashboard use this url: http://0.0.0.0:8001/docs

### FastAPI Demonstration

The Following command runs the FastAPI testing app

```bash
uvicorn main:app --reload
```

Using the localhost url, we can see the following demos


