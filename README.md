# MLOps Assignment 1 — Breast Cancer Classification

| | |
|---|---|
| **Name** | Aousaf Sulaman |
| **Roll Number** | 25L-8013 |
| **Repository** | [mlops-project-25L-8013](https://github.com/Aousaf90/mlops-project-25L-8013) |

Trains a Logistic Regression classifier on the breast cancer dataset and saves the model to `model/`. Raw data and model artifacts are excluded from Git via `.gitignore`.

## Project structure

```text
data/                  # raw dataset (ignored)
src/train_25L8013.py   # training script
model/                 # saved model output (ignored)
requirements.txt
.gitignore
README.md
```

## Setup

From the repository root:

```bash
conda create --name mlops --file requirements.txt
conda activate mlops
```

Place `breast_cancer.csv` in `data/` before training.

## Run training

```bash
python src/train_25L8013.py
```

The trained model is written to `model/logistic_regression_model.joblib`.
