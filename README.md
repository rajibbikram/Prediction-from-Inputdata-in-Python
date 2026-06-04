📊 Prediction from Input Data in Python

A Machine Learning Web Application that predicts student performance based on academic and demographic inputs using a trained regression model and Flask backend.

🚀 Live Demo

(Add deployment link here if hosted)
http://127.0.0.1:5000/

🧠 Project Overview

This project uses Machine Learning (Random Forest Regressor) to predict a student's final performance score based on multiple features such as gender, race, parental education, and exam scores.

It includes:

Data preprocessing with OneHotEncoder
Model training with Scikit-learn
Flask web app for real-time prediction
Saved model using joblib
⚙️ Tech Stack
🐍 Python
📊 Pandas, NumPy
🤖 Scikit-learn
🌐 Flask
💾 Joblib
🎨 HTML/CSS (Frontend)
📁 Project Structure
PythonMlTask/
│
├── train.ipynb              # Model training notebook
├── app.py                   # Flask backend
├── StudentsPerformance.csv  # Dataset
├── model.pkl                # Trained model
├── preprocessor.pkl         # Preprocessing pipeline
│
└── templates/
    └── index.html          # Frontend UI
🧾 Input Features
Feature	Type
Gender	Categorical
Race/Ethnicity	Categorical
Parental Education	Categorical
Lunch Type	Categorical
Test Preparation	Categorical
Math Score	Numerical
Reading Score	Numerical
Writing Score	Numerical
🔮 Model Output

The system predicts:

Final Performance Score

Example:

82.45
📥 Example Input
{
    "gender": "female",
    "race/ethnicity": "group B",
    "parental level of education": "bachelor's degree",
    "lunch": "standard",
    "test preparation course": "none",
    "math score": 70,
    "reading score": 80,
    "writing score": 75
}
▶️ How to Run Locally
1️⃣ Train Model
jupyter notebook train.ipynb

This generates:

model.pkl
preprocessor.pkl
2️⃣ Run Flask App
python app.py
3️⃣ Open in Browser
http://127.0.0.1:5000/
⚠️ Important Notes
Input column names must match training dataset exactly
Always use DataFrame for prediction input
Preprocessor must be applied before prediction
🧠 Machine Learning Pipeline

Dataset → Preprocessing → Train Model → Save Model → Flask App → Prediction
