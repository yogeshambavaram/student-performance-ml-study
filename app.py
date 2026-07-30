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
st.markdown("""
# 🎓 Student Performance Predictor

### 🤖 AI-powered Grade Prediction
""")

st.set_page_config(
    page_title="Student Academic Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Academic Performance Predictor")

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

studytime = st.select_slider(
    "📚 Daily Study Time",
    options=[
        "< 2 hours",
        "2–5 hours",
        "5–10 hours",
        "> 10 hours"
    ],
    value="2–5 hours"
)

studytime_map = {
    "< 2 hours": 1,
    "2–5 hours": 2,
    "5–10 hours": 3,
    "> 10 hours": 4
}

studytime = studytime_map[studytime]
)

traveltime = st.select_slider(
    "🚌 Travel Time",
    options=[
        "< 15 minutes",
        "15–30 minutes",
        "30–60 minutes",
        "> 60 minutes"
    ],
    value="< 15 minutes"
)

travel_map = {
    "< 15 minutes": 1,
    "15–30 minutes": 2,
    "30–60 minutes": 3,
    "> 60 minutes": 4
}

traveltime = travel_map[traveltime]
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

if st.button("🎯 Predict Grade", use_container_width=True):

    prediction = model.predict(input_data)[0]

    st.header("Prediction")

    st.metric(
        label="Predicted Final Grade",
        value=f"{prediction:.1f} / 20"
    )

   st.metric(
    "Predicted Grade",
    f"{prediction:.1f}/20",
    help="Predicted final academic grade"
)

    if prediction >= 16:
        st.success("🌟 Excellent predicted academic performance!")
        st.balloons()

    elif prediction >= 10:
        st.info("📘 Average predicted academic performance.")

    else:
        st.warning("⚠️ Predicted below the passing grade.")

    st.info("The UCI dataset uses a grading scale from **0 to 20**.")

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
