# 📊 Student Performance Prediction

## 📌 Project Overview
This project uses **Machine Learning** to predict a student's **final exam grade (G3)** based on their study habits and previous academic performance. The model analyzes important factors like **study time, absences, and previous grades** to estimate the final result.

The project demonstrates the **complete Machine Learning workflow**, including data analysis, visualization, model training, and evaluation.

---

## 🎯 Problem Statement
Predict the **final student grade (G3)** using previous academic performance and study-related features.

---

## 📥 Input Features
The following features are used as input variables for the machine learning model:

- **Study time** – Weekly study time of the student  
- **Absences** – Number of school absences  
- **G1** – First period grade  
- **G2** – Second period grade  

### Example Input
study_time = 3
absences = 5
G1 = 12
G2 = 13


---

## 📤 Output (Target Variable)

The model predicts:

**G3 – Final Grade**

### Example Output
Predicted Final Grade (G3) = 14


This helps estimate how well a student might perform in the final exam.

---

## ⚙️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🤖 Machine Learning Models Used

### 1️⃣ Linear Regression
Used to predict the final grade based on a linear relationship between the input features and the target variable.

### 2️⃣ Random Forest Regressor
An ensemble machine learning model used to improve prediction accuracy and identify feature importance.

---

## 📊 Model Evaluation
The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

These metrics help measure how accurately the model predicts student grades.

---

## 📈 Key Insights
- Previous grades (**G1 and G2**) are the most important factors in predicting the final grade.
- Study time also affects performance.
- Random Forest model provides better prediction accuracy compared to Linear Regression.

---

## 📁 Project Structure
Student-Performance-Prediction
│
├── student_data.csv
├── student_performance.ipynb
├── README.md


---

## 🚀 Future Improvements
- Add more machine learning models
- Deploy the project using **Streamlit Web App**
- Create an interactive dashboard for predictions
