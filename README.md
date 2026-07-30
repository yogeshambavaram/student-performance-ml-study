# Predicting Student Academic Performance Using Machine Learning

## Overview

This project investigates whether demographic, family, and lifestyle factors can predict students' final academic performance.

Unlike many existing studies, previous grades (G1 and G2) were intentionally excluded to prevent data leakage and evaluate the predictive power of non-academic variables alone.

---

## Research Question

Can demographic, family, and lifestyle characteristics predict students' final grades without using previous academic performance?

---

## Dataset

- UCI Student Performance Dataset
- 395 students
- 30 input features after preprocessing
- Target: Final Grade (G3)

---

## Machine Learning Models

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

---

## Evaluation Metrics

- MAE
- RMSE
- R² Score
- 5-Fold Cross Validation

---

## Results

| Model | R² |
|-------|----|
| Linear Regression | 0.141 |
| Gradient Boosting | 0.209 |
| Random Forest | **0.270** |

---

## Feature Importance

*(Insert your feature importance image here)*

---

## Repository Structure

*(Tree view)*

---

## Future Work

- Larger datasets
- Hyperparameter tuning
- Additional regression models
- Interactive Streamlit application

---

## Author

Yogesh Ambavaram
