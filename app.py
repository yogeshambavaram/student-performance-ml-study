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

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#172554,#0f766e);
background-size:300% 300%;
animation:gradient 12s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Sidebar */
[data-testid="stSidebar"]{
background:rgba(20,20,30,0.65);
backdrop-filter:blur(18px);
}

/* Buttons */
.stButton>button{
border-radius:12px;
height:3.2em;
font-size:18px;
font-weight:600;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.03);
}

/* Metric cards */
[data-testid="metric-container"]{
background:rgba(255,255,255,0.08);
padding:18px;
border-radius:18px;
backdrop-filter:blur(12px);
}

</style>
""", unsafe_allow_html=True)

st.title("🎓 EduPredict AI")
st.subheader("AI-powered Student Performance Prediction")

st.info(
    "📚 Enter a student's academic and lifestyle information to receive an estimated final grade and personalized recommendations."
)

# 👇 ADD TABS HERE
tab1, tab2, tab3 = st.tabs([
    "🎯 Predictor",
    "📊 Model Insights",
    "ℹ️ About"
])

 # =====================================
# TAB 1 - PREDICTOR
# =====================================

with tab1:

    st.write("Use the sidebar to enter the student's information.")

    # Your prediction code starts here
    # (Sidebar stays outside tabs because Streamlit sidebars are global)

    

# =====================================
# TAB 2 - MODEL INSIGHTS
# =====================================

with tab2:

    st.header("📊 Model Insights")

    st.write("### Model Comparison")

    st.table({
        "Model": [
            "Linear Regression",
            "Random Forest",
            "Gradient Boosting"
        ],
        "R² Score": [
            0.27,
            0.13,
            0.21
        ]
    })

    st.markdown("---")

    st.write("### Dataset")

    st.write("• 395 student records")
    st.write("• 33 original features")
    st.write("• Random Forest selected for deployment")

# =====================================
# TAB 3 - ABOUT
# =====================================

with tab3:

    st.header("ℹ️ About EduPredict AI")

    st.write("""
This application predicts student academic performance using a
Random Forest Regression model.

### Technologies
- Python
- pandas
- scikit-learn
- Streamlit
- Joblib

### Dataset
Student Performance Dataset from the
University of California, Irvine (UCI)
Machine Learning Repository.
""")

    st.success("👨‍💻 Developed by Yogesh Ambavaram")
       
# Animation goes HERE

st.markdown("""
Predict a student's final academic grade using a Random Forest Machine Learning model.
""")

st.markdown("""
Predict a student's **final academic grade** using a Random Forest Machine Learning model trained on the **UCI Student Performance Dataset**.

Adjust the inputs below and click **Predict Grade**.
""")

st.markdown("---")

# ==================================
# SIDEBAR
# ==================================

st.sidebar.image(
    "https://img.icons8.com/color/96/graduation-cap.png",
    width=80
)

st.sidebar.title("🎓 EduPredict AI")
st.sidebar.caption("Student Profile")

st.sidebar.markdown("---")

# ==========================
# Personal
# ==========================

with st.sidebar.expander("👤 Personal Information", expanded=True):

    age = st.slider(
        "🎂 Age",
        15,
        22,
        17
    )

# ==========================
# Academics
# ==========================

with st.sidebar.expander("📚 Academic Habits", expanded=True):

    studytime_label = st.select_slider(
        "📖 Daily Study Time",
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

    studytime = studytime_map[studytime_label]

    traveltime_label = st.select_slider(
        "🚌 Daily Travel Time",
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

    traveltime = travel_map[traveltime_label]

    failures = st.slider(
        "❌ Previous Academic Failures",
        0,
        4,
        0
    )

    absences = st.slider(
        "🏫 School Absences",
        0,
        50,
        5
    )

# ==========================
# Lifestyle
# ==========================

with st.sidebar.expander("❤️ Lifestyle", expanded=True):

    health = st.slider(
        "Health Rating",
        1,
        5,
        3,
        help="1 = Very Poor | 5 = Excellent"
    )

    famrel = st.slider(
        "Family Relationship",
        1,
        5,
        4,
        help="1 = Very Bad | 5 = Excellent"
    )

    freetime = st.slider(
        "Free Time After School",
        1,
        5,
        3
    )

    goout = st.slider(
        "Social Outings",
        1,
        5,
        3
    )

st.sidebar.markdown("---")

st.sidebar.success(
    "💡 Adjust the student's profile and click **Predict Grade**."
)
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
