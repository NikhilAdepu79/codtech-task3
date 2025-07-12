#END-TO-END DATA SCIENCE PROJECT

COMPANY: CODTECH IT SOLUTIONS

NAME: ADEPU NIKHIL

"INTERN ID: CT06DF1201

"DOMAIN: DATA SCIENCE

"DURATION: 6 WEEKS

"MENTOR: NEELA SANTOSH

DESCRIPTION OF THIS TASK

# 🌼 Task 3 – Iris Flower Classification API

This project is part of my **CodTech Internship Task 3**, where I developed an end-to-end data science pipeline and deployed a machine learning model using **FastAPI**.

---

## ✅ Objective

The goal is to build a machine learning model that classifies **Iris flowers** into three species:  
- **Setosa**  
- **Versicolor**  
- **Virginica**  

The model is trained using `scikit-learn`, and deployed as an API using **FastAPI**.

---

## 🛠️ Technologies Used

- **Python**
- **scikit-learn** for model building
- **FastAPI** for creating the API
- **Uvicorn** for running the server
- **Joblib** for saving the model

---

## 🚀 Features

- Trains a logistic regression model on the Iris dataset.
- Predicts species based on sepal and petal measurements.
- Provides predictions via a RESTful API.
- Lightweight, fast, and easy to run.

---

## ▶️ How to Run

### 1. Install Required Packages
bash
pip install fastapi uvicorn scikit-learn pandas joblib
run the fastapi server:
uvicorn main:app --reload
go to http://127.0.0.1:8000
example output:{"prediction": "Setosa"}


#output screenshot:
<img width="1901" height="699" alt="Image" src="https://github.com/user-attachments/assets/5c90aac3-df84-4d73-bd34-427b37d44c55" />


