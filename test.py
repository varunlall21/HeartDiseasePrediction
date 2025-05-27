import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load("xgboost_heart_model.pkl")

# Page title
st.title("❤️ Heart Disease Prediction")
st.write("Enter your health parameters below:")

# Input fields
age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
chol = st.number_input("Cholesterol (chol)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (fbs)", [0, 1])
restecg = st.selectbox("Rest ECG results (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved (thalach)", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST depression (oldpeak)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of ST segment", [0, 1, 2])
ca = st.selectbox("Number of major vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

# Map inputs to model format
sex_val = 1 if sex == "Male" else 0

input_data = np.array([[age, sex_val, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of Heart Disease!")
    else:
        st.success("✅ No Heart Disease detected.")

