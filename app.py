import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title Section
st.title("🎓 Student Performance Prediction System")
st.markdown("### Predict a student's final exam grade using Machine Learning")

st.write(
"This web application predicts the **Final Grade (G3)** of a student "
"based on study behavior and previous academic performance."
)

# Load Dataset
df = pd.read_csv("student_data.csv")

# Features
X = df[["studytime","absences","G1","G2"]]
y = df["G3"]

# Train Model
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor()
model.fit(X_train,y_train)

# Divider
st.markdown("---")

# Input Section
st.header("📥 Enter Student Details")

col1,col2 = st.columns(2)

with col1:
    studytime = st.slider("Study Time (1-4)",1,4,2)
    absences = st.number_input("Number of Absences",0,100,5)

with col2:
    G1 = st.number_input("First Period Grade (G1)",0,20,10)
    G2 = st.number_input("Second Period Grade (G2)",0,20,12)

st.markdown("---")

# Prediction
if st.button("🔮 Predict Final Grade"):

    input_data = pd.DataFrame(
        [[studytime,absences,G1,G2]],
        columns=["studytime","absences","G1","G2"]
    )

    prediction = model.predict(input_data)

    st.success(f"🎯 Predicted Final Grade (G3): {round(prediction[0],2)}")

# Footer
st.markdown("---")
st.markdown("👩‍💻 Developed by **Leetika | Data Science Intern**")