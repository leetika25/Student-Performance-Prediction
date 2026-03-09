# 🎓 Student Performance Prediction

## 📌 Project Overview

Student performance prediction is an important problem in the field of **Educational Data Mining**.  
This project uses **Machine Learning algorithms** to predict a student's **final exam grade (G3)** based on their previous academic performance and study behavior.

The model analyzes factors such as **study time, absences, and previous grades** to estimate how a student might perform in the final exam.

This project demonstrates a **complete Machine Learning workflow**, including:

- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Model Training
- Model Evaluation

---

# 🎯 Problem Statement

The objective of this project is to **predict the final grade (G3)** of a student using previous academic performance and study-related features.

Predicting student performance can help educators:

- Identify struggling students early
- Provide academic support
- Improve learning outcomes

---

# 📊 Dataset Information

The dataset contains student academic information such as:

- Study habits
- Attendance
- Previous grades

### Key Features Used

| Feature | Description |
|------|-------------|
| studytime | Weekly study time |
| absences | Number of school absences |
| G1 | First period grade |
| G2 | Second period grade |
| G3 | Final grade (Target Variable) |

---

# 📥 Example Input

```
studytime = 3
absences = 5
G1 = 12
G2 = 13
```

# 📤 Predicted Output

```
Predicted Final Grade (G3) = 14
```

---

# ⚙️ Technologies Used

- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical computing
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Scikit-learn** – Machine learning models

---

# 🤖 Machine Learning Models

## 1️⃣ Linear Regression
A basic regression model used to predict the final grade based on a linear relationship between input features and the target variable.

## 2️⃣ Random Forest Regressor
An ensemble machine learning algorithm that improves prediction accuracy by combining multiple decision trees.

---

# 📊 Model Evaluation

The models were evaluated using the following metrics:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R² Score**

These metrics measure how well the model predicts the final grade.

---

# 📈 Key Insights

- Previous grades (**G1 and G2**) are the **strongest predictors** of the final grade.
- Students with **higher study time generally perform better**.
- **Random Forest Regressor performed better** than Linear Regression in prediction accuracy.

---

# 📁 Project Structure

```
Student-Performance-Prediction
│
├── student_data.csv                # Dataset
├── student_performance.ipynb       # ML model and analysis
└── README.md                       # Project documentation
```

---

# 🚀 Future Improvements

- Build more advanced models (XGBoost, Gradient Boosting)
- Deploy the model using **Streamlit Web App**
- Create an **interactive dashboard**
- Use more features for better prediction accuracy

---

# 👩‍💻 Author

**Leetika**

Data Science Enthusiast | Machine Learning Learner

---
