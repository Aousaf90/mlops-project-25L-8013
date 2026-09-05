import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

import joblib


# ==========================================
# 1. Load dataset
# ==========================================

df = pd.read_csv("data/breast_cancer.csv")

print("Dataset shape:", df.shape)
print(df.head())


# ==========================================
# 2. Separate features and target
# ==========================================

X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]


# ==========================================
# 3. Train/test split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 4. Create Logistic Regression pipeline
# ==========================================

model = Pipeline([
    ("normalizer", MinMaxScaler()),  # data normalization step
    ("logistic_regression", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])


# ==========================================
# 5. Train model
# ==========================================

model.fit(X_train, y_train)


# ==========================================
# 6. Evaluate model
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Benign", "Malignant"]
))


# ==========================================
# 7. Save trained model
# ==========================================

joblib.dump(
    model,
    "model/logistic_regression_model.joblib"
)

print("\nModel saved successfully!")
print("File: logistic_regression_model.joblib")
