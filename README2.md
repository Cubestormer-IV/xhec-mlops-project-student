<div align="center">

# Prediction of Abalone Age

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: flake8](https://img.shields.io/badge/linting-flake8-yellowgreen.svg)](https://flake8.pycqa.org/)

</div>

## Context of the project

### Description
This repository has for purpose to industrialize the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) Kaggle contest.

The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

**Objective**: predict the age of abalone (Rings + 1.5) from various physical measurements.

**Dataset**: The dataset is available to download at [Kaggle page](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset).

**Authors**: [Eva Toledano](https://github.com/eva-toledano), [Qiling Zhu](https://github.com/qly0923), [Khushi Verma](https://github.com/khushiverma12
), [Elise Barattini](https://github.com/ebarattini), [Tanmay Kale](https://github.com/Cubestormer-IV)

## Recreating the python environment

Use a virtual environment to install the dependencies of the project:
```bash
conda env create --file environment.yml
conda activate <envname>
```

## Running the code
### Running the API

To get access to the FastAPI dashboard use this url: TODO

### Building the Docker Image

