import streamlit as st
import pandas as pd
import joblib

# ===============================
# Page Title
# ===============================
st.markdown(
    "<h1 style='text-align:center;'>🚢 Titanic Survival Prediction</h1>",
    unsafe_allow_html=True
)

# ===============================
# Load Trained Model
# ===============================
model = joblib.load("model1.pkl")

# ===============================
# User Inputs
# ===============================
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sibsp = st.number_input("Siblings / Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents / Children Aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0)
embarked = st.selectbox("Embarked Port", ["S", "C", "Q"])

# ===============================
# Manual Encoding (IMPORTANT)
# ===============================
sex_map = {"male": 0, "female": 1}
embarked_map = {"S": 0, "C": 1, "Q": 2}

sex_encoded = sex_map[sex]
embarked_encoded = embarked_map[embarked]

# ===============================
# Create Input DataFrame
# (ORDER MUST MATCH TRAINING)
# ===============================
input_data = pd.DataFrame([[
    pclass,
    sex_encoded,
    age,
    sibsp,
    parch,
    fare,
    embarked_encoded
]], columns=[
    "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"
])

# ===============================
# Prediction
# ===============================
if st.button("Predict Survival"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")
