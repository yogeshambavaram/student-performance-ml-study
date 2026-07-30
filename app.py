import streamlit as st
import pandas as pd
import joblib

# Load trained model and feature names
model = joblib.load("student_grade_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.set_page_config(page_title="Student Grade Predictor", page_icon="🎓")

st.title("🎓 Student Academic Performance Predictor")

st.write(
    "Predict a student's final grade using a machine learning model trained on demographic, family, and lifestyle data."
)

# --------------------
# User Inputs
# --------------------

age = st.slider("Age", 15, 22, 17)

studytime = st.slider("Study Time (1-4)", 1, 4, 2)

failures = st.slider("Previous Failures", 0, 4, 0)

absences = st.slider("Absences", 0, 50, 5)

health = st.slider("Health (1-5)", 1, 5, 3)

famrel = st.slider("Family Relationship (1-5)", 1, 5, 4)

freetime = st.slider("Free Time (1-5)", 1, 5, 3)

goout = st.slider("Going Out (1-5)", 1, 5, 3)

traveltime = st.slider("Travel Time (1-4)", 1, 4, 1)

# --------------------
# Create input dataframe
# --------------------

input_data = pd.DataFrame(0, index=[0], columns=feature_names)

# Fill numerical features
input_data["age"] = age
input_data["studytime"] = studytime
input_data["failures"] = failures
input_data["absences"] = absences
input_data["health"] = health
input_data["famrel"] = famrel
input_data["freetime"] = freetime
input_data["goout"] = goout
input_data["traveltime"] = traveltime

# --------------------
# Prediction
# --------------------

if st.button("Predict Grade"):

    prediction = model.predict(input_data)[0]

    st.success(f"🎯 Predicted Final Grade: {prediction:.1f} / 20")

    st.info("📘 Note: The dataset uses a grading scale from 0 to 20.")

    if prediction < 10:
        st.error("⚠️ Predicted below the passing grade.")
    elif prediction < 15:
        st.info("📚 Predicted average academic performance.")
    else:
        st.success("🌟 Predicted strong academic performance!")
