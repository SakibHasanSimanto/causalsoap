# causalsoap

**Causal Feature Selection and Dimensionality Reduction using Residual-Based ATE Estimation**  
Author: [Kazi Sakib Hasan](mailto:simanto.alt@gmail.com)

---

## 🔰 What is causalsoap?

`causalsoap` is a Python library for **causal inference-driven feature selection and dimensionality reduction technique**.  
It ranks features based on their **Average Treatment Effect (ATE)** on an outcome variable by applying the **Frisch–Waugh–Lovell (FWL) theorem** using residualization and double machine learning.

This method is particularly useful when:
- You want **interpretable** ranking of features by causal effect
- The dataset has **confounders**
- Traditional correlation-based selection is misleading

Link to preprint will be available soon. 

---

## 📦 Installation

```bash
pip install causalsoap
```
## 🚀 Quickstart 
```
import pandas as pd
import numpy as np
from causalsoap import CausalDRIFT

# Simulated data
df = pd.DataFrame({
    'X1': np.random.randn(100),
    'X2': np.random.rand(100),
    'X3': np.random.randn(100),
    'X4': np.random.choice([0, 1, 2], size=100),  # categorical numeric
    'Y': np.random.randn(100)
})

# Run model
X = df.drop(columns='Y')
y = df['Y']

model = CausalDRIFT()
model.fit(X, y, outcome_type='continuous', categorical_features=['X4'])

print(model.get_feature_ate())
```
## ⚙️ Parameters
```
fit(X, y, outcome_type, categorical_features=None) 
```
`X` : Feature matrix (all numeric) `pd.DataFrame`
`y` : Target variable `pd.Series`
`outcome_type` : Continuous or categorical `str`
`categorical_features`: List of column names in `X` that are categorical but encoded numerically `list[str]`

## 📈 How it Works

For each feature:

1.  Predict the **outcome** using confounders → compute residual (`Ro`)
    
2.  Predict the **feature (treatment)** using confounders → residual (`Rt`)
    
3.  Estimate ATE via linear regression: `Ro ~ Rt`

## 💡Interpretation 

Consider: ATE of 'X1' on Y = +2.5 

This means: 
If you increased 'X1' by 1 unit, holding confounders constant,
the outcome Y would increase by 2.5 on average. 

## Reproducibility of Research 
Algorithm codes: https://colab.research.google.com/drive/12lIFDuD9k-qxLA9UcBm3-0Eq9YC3V8T_?usp=sharing  

Analysis on Breast Cancer datset: https://colab.research.google.com/drive/1ScKgbHQysVOpECc8NZ_Tz-lY2MmUiXov?usp=sharing 

Analysis on Diabetes dataset: https://colab.research.google.com/drive/165H4_j-mJsDsp9Vi4gkBbcrH02qq-nhu?usp=sharing 

Analysis on Heart disease dataset: https://colab.research.google.com/drive/1efgUr8biLaAWRsTbJ0gHJtZgvFc63nW6?usp=sharing  

Analysis on PCOS dataset: https://colab.research.google.com/drive/1HIGl0EjO76UgK00w7bXt1A9fkbu0F3X6?usp=sharing 

