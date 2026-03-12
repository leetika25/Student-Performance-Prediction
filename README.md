# 🎓 Student Performance Prediction System

A Machine Learning web application that predicts a student's **Final Exam Grade (G3)** based on study habits and previous academic performance.

This project demonstrates the complete **Machine Learning lifecycle** including data preprocessing, model training, evaluation, and deployment using **Streamlit**.

---

# 🚀 Live Web Application

🔗 **Live Demo:**  
https://student-performance-prediction-spp.streamlit.app/

---

# 🎥 Demo Video




https://github.com/user-attachments/assets/7e8a214b-c123-466e-be51-502211ea720d



---

# 📌 Project Overview

Educational institutions often want to identify students who may struggle academically.  
This project predicts the **final student grade (G3)** using key academic indicators such as:

- Study Time
- Number of Absences
- First Period Grade (G1)
- Second Period Grade (G2)

The Machine Learning model learns patterns from historical student data and predicts the expected final exam score.

---

# 📊 Input Features

| Feature | Description |
|-------|-------------|
| Study Time | Weekly study time (scale 1–4) |
| Absences | Total number of school absences |
| G1 | First period grade |
| G2 | Second period grade |

---

# 🎯 Target Variable

| Variable | Description |
|--------|-------------|
| G3 | Final Exam Grade |

---

# 🧠 Machine Learning Workflow

1️⃣ Data Collection  
2️⃣ Data Cleaning & Preprocessing  
3️⃣ Exploratory Data Analysis (EDA)  
4️⃣ Feature Selection  
5️⃣ Model Training  
6️⃣ Model Evaluation  
7️⃣ Model Deployment using Streamlit  

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# 📂 Project Structure

```
Student-Performance-Prediction
│
├── app.py                     # Streamlit Web Application
├── student_data.csv           # Dataset
├── student_performance.ipynb  # Model Training Notebook
├── model.pkl                  # Trained ML Model
├── requirements.txt           # Dependencies
├── demo_video.mp4             # Project Demo Video
└── README.md                  # Project Documentation
```

---

# ⚙️ Installation & Setup

### Clone the repository

```
git clone https://github.com/your-username/student-performance-prediction.git
```

### Navigate to project directory

```
cd student-performance-prediction
```

### Install required libraries

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

---

# 📈 Model Prediction Logic

The model predicts the final grade based on patterns learned from historical student performance data.

Previous grades (**G1 and G2**) have the **strongest correlation with final grade (G3)**, making them key predictors in the model.

---

# 🌟 Key Features

✔ Interactive Streamlit Web Interface  
✔ Real-time Grade Prediction  
✔ Machine Learning Model Integration  
✔ Clean and User-Friendly UI  
✔ Deployable ML Application  

---

# 📚 Dataset

The project uses the **Student Performance Dataset**, which contains academic and behavioral attributes of students used to predict final grades.

---

# 👩‍💻 Author

**Leetika**

Aspiring **Data Scientist | Machine Learning Enthusiast**

---
