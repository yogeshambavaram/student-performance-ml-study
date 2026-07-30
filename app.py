import streamlit as st
import pandas as pd
import joblib

# -----------------------------------
# Load trained model
# -----------------------------------

model = joblib.load("student_grade_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Student Academic Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduPredict AI")
st.subheader("AI-powered Student Performance Prediction")

st.info(
    "📚 Enter a student's academic and lifestyle information to receive an estimated final grade and personalized recommendations."
)

# Animation goes HERE

st.markdown("""
Predict a student's final academic grade using a Random Forest Machine Learning model.
""")

st.markdown("""
Predict a student's **final academic grade** using a Random Forest Machine Learning model trained on the **UCI Student Performance Dataset**.

Adjust the inputs below and click **Predict Grade**.
""")

st.markdown("---")

# -----------------------------------
# User Inputs
# -----------------------------------

age = st.slider(
    "🎂 Age",
    15, 22, 17
)

studytime = st.slider(
    "📚 Daily Study Time\n(1 = <2 hrs | 2 = 2–5 hrs | 3 = 5–10 hrs | 4 = >10 hrs)",
    1, 4, 2
)

traveltime = st.slider(
    "🚌 Travel Time to School\n(1 = <15 min | 2 = 15–30 min | 3 = 30–60 min | 4 = >60 min)",
    1, 4, 1
)

health = st.slider(
    "❤️ Health Rating\n(1 = Very Poor | 5 = Excellent)",
    1, 5, 3
)

famrel = st.slider(
    "👨‍👩‍👧 Family Relationship\n(1 = Very Bad | 5 = Excellent)",
    1, 5, 4
)

freetime = st.slider(
    "⏰ Free Time After School\n(1 = Very Little | 5 = A Lot)",
    1, 5, 3
)

goout = st.slider(
    "🎉 Social Outings\n(1 = Very Rarely | 5 = Very Frequently)",
    1, 5, 3
)

failures = st.slider(
    "❌ Previous Academic Failures",
    0, 4, 0
)

absences = st.slider(
    "🏫 Number of School Absences",
    0, 50, 5
)

st.markdown("---")

# -----------------------------------
# Create Input Data
# -----------------------------------

input_data = pd.DataFrame(0, index=[0], columns=feature_names)

input_data["age"] = age
input_data["studytime"] = studytime
input_data["traveltime"] = traveltime
input_data["health"] = health
input_data["famrel"] = famrel
input_data["freetime"] = freetime
input_data["goout"] = goout
input_data["failures"] = failures
input_data["absences"] = absences

# -----------------------------------
# Prediction
# -----------------------------------

import time

if st.button("🎯 Predict Grade", use_container_width=True):

    prediction_placeholder = st.empty()

    prediction_placeholder.info("🤖 AI is analyzing your academic profile...")
    time.sleep(1)

    prediction_placeholder.info("📊 Evaluating study habits and attendance...")
    time.sleep(1)

    prediction_placeholder.info("🧠 Running Random Forest prediction model...")
    time.sleep(1)

    prediction = model.predict(input_data)[0]

    prediction_placeholder.empty()

    st.markdown("## 🎯 Prediction Result")

    st.metric(
        label="Predicted Final Grade",
        value=f"{prediction:.1f} / 20",
        delta=f"{prediction/20*100:.0f}%"
    )

    st.progress(prediction / 20)

    if prediction >= 16:
        st.success("🌟 Excellent predicted academic performance!")
        st.balloons()

    elif prediction >= 10:
        st.info("📘 Average predicted academic performance. Small improvements could increase the predicted score.")

    else:
        st.warning("⚠️ Predicted below the passing grade. Consider the recommendations below.")

    st.info("📘 This model predicts grades on a 0–20 scale used in the original dataset.")

    st.markdown("---")
    # -----------------------------------
    # Strengths & Suggestions
    # -----------------------------------

    strengths = []
    suggestions = []

    # Study Time
    if studytime >= 3:
        strengths.append("📚 Strong study habits.")
    else:
        suggestions.append("Increase your daily study time by 1–2 hours.")

    # Attendance
    if absences <= 5:
        strengths.append("🏫 Good attendance.")
    else:
        suggestions.append("Reduce school absences to improve learning consistency.")

    # Health
    if health >= 4:
        strengths.append("❤️ Good overall health.")
    else:
        suggestions.append("Improve sleep, nutrition, and physical activity.")

    # Family
    if famrel >= 4:
        strengths.append("👨‍👩‍👧 Strong family support.")
    else:
        suggestions.append("Build a stronger support system with family or mentors.")

    # Social Life
    if goout <= 3:
        strengths.append("🎯 Healthy balance between study and social life.")
    else:
        suggestions.append("Reduce social outings during important academic periods.")

    # Previous Failures
    if failures == 0:
        strengths.append("✅ No previous academic failures.")
    else:
        suggestions.append("Spend extra time reviewing subjects you've previously struggled with.")

    # -----------------------------------
    # Display Strengths
    # -----------------------------------

    if strengths:
        st.subheader("✅ Strengths")

        for item in strengths:
            st.write("•", item)

    # -----------------------------------
    # Display Suggestions
    # -----------------------------------

    if suggestions:
        st.subheader("💡 Suggestions to Improve")

        for item in suggestions:
            st.write("•", item)
    else:
        st.success("Excellent! No major improvement areas were identified from the selected inputs.")

    st.markdown("---")

    st.caption(
        "Developed by Yogesh Ambavaram | Random Forest Regression | UCI Student Performance Dataset"
    )

    st.caption(
        "Disclaimer: This prediction is generated by a machine learning model and is intended for educational purposes only. "
        "It provides an estimate based on the selected inputs and should not be considered an official academic evaluation."
    )
