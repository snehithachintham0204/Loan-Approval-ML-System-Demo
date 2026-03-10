# 🏦 FinTrust AI – Intelligent Loan & Risk Decision Engine

## 📌 Overview
FinTrust AI is an Artificial Intelligence based loan approval and risk assessment system that helps predict whether a loan will be approved or rejected based on financial and personal parameters.

The system uses Machine Learning algorithms to analyze loan data and provide instant predictions. It also calculates risk percentage, EMI, total repayment amount, and provides financial suggestions for improving loan eligibility.

This project demonstrates how Artificial Intelligence can be applied in banking systems to automate loan evaluation, reduce manual errors, and support faster decision-making.

---

# 🎯 Project Objectives
- Build a machine learning model to predict loan approval.
- Compare multiple ML algorithms and select the best performing model.
- Deploy the trained model into a real-time web application.
- Provide financial insights such as EMI calculation and risk analysis.
- Improve accessibility through multilingual voice assistance.

---

# ⚙️ Technologies Used

## Programming Language
- Python

## Machine Learning Libraries
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Models Implemented
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- **AdaBoost (Selected Model)**

## Deployment
- Streamlit (Web Application)

## Additional Libraries
- gTTS (Google Text-to-Speech)

---

# 📊 Machine Learning Methodology

### 1️⃣ Dataset Preparation
The loan dataset was loaded and prepared for training.

### 2️⃣ Data Preprocessing
- Handling missing values
- Cleaning incorrect data
- Data formatting

### 3️⃣ Feature Encoding
Categorical variables such as:
- Gender
- Education
- Property Area

were converted into numerical values to be used by machine learning algorithms.

### 4️⃣ Train-Test Split
The dataset was divided into:
- Training Data
- Testing Data

This allows the model to be evaluated on unseen data.

### 5️⃣ Model Training
Multiple machine learning algorithms were trained including:

- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

### 6️⃣ Model Comparison
All models were evaluated using accuracy metrics and compared.

### 7️⃣ Model Selection
AdaBoost achieved the best performance and was selected as the final model.

### 8️⃣ Model Saving
The trained model was saved using Joblib as:
loan_model.pkl
model_columns.pkl


This allows the model to be reused without retraining.

---

# 🌐 Web Application Development

The trained machine learning model was integrated into a **Streamlit web application**.

Users can enter personal and financial information including:

- Full Name
- Email ID
- Mobile Number
- Date of Birth
- Gender
- Marital Status
- Dependents
- Education
- Employment Type
- Monthly Income
- Loan Amount
- Loan Tenure
- Credit History
- Property Area

After entering the details, the system evaluates the loan application instantly.

---

# 📈 Loan Decision System

The system predicts:

- **Loan Approved**
or
- **Loan Rejected**

It also calculates:

- Risk Percentage
- Risk Level (Low / Moderate / High)

---

# 💰 EMI Calculation

If the loan is approved, the system calculates EMI using the standard banking formula.

### EMI Formula

Where:

- **P** = Loan Amount  
- **r** = Monthly Interest Rate  
- **n** = Loan Term in Months  

The system also calculates:

- Monthly EMI
- Total Interest
- Total Repayment Amount

---

# 🧠 Financial Advisory System

If the loan is rejected, the system provides possible reasons such as:

- Poor credit history
- High debt-to-income ratio
- Low income
- High loan amount

It also suggests improvements such as:

- Reduce loan amount
- Improve credit score
- Maintain stable income

---

# 🔊 Multilingual Voice Assistance

The application includes voice assistance using **Google Text-to-Speech (gTTS)**.

Features include:

- Voice instructions for each input field
- Voice output for results
- Multi-language support

Supported languages:

- English
- Hindi
- Telugu

This improves accessibility for users who may not be comfortable with text-based interfaces.

---

# 🚀 Key Features

- AI Based Loan Approval Prediction
- Risk Percentage Calculation
- EMI & Repayment Calculation
- Financial Suggestions for Loan Improvement
- Multilingual Voice Assistance
- User-Friendly Web Interface
- Real-Time Loan Decision System

---

# 🖥 How to Run the Project

### Install Required Libraries

Where:

- **P** = Loan Amount  
- **r** = Monthly Interest Rate  
- **n** = Loan Term in Months  

The system also calculates:

- Monthly EMI
- Total Interest
- Total Repayment Amount

---

# 🧠 Financial Advisory System

If the loan is rejected, the system provides possible reasons such as:

- Poor credit history
- High debt-to-income ratio
- Low income
- High loan amount

It also suggests improvements such as:

- Reduce loan amount
- Improve credit score
- Maintain stable income

---

# 🔊 Multilingual Voice Assistance

The application includes voice assistance using **Google Text-to-Speech (gTTS)**.

Features include:

- Voice instructions for each input field
- Voice output for results
- Multi-language support

Supported languages:

- English
- Hindi
- Telugu

This improves accessibility for users who may not be comfortable with text-based interfaces.

---

# 🚀 Key Features

- AI Based Loan Approval Prediction
- Risk Percentage Calculation
- EMI & Repayment Calculation
- Financial Suggestions for Loan Improvement
- Multilingual Voice Assistance
- User-Friendly Web Interface
- Real-Time Loan Decision System

---

# 🖥 How to Run the Project

### Install Required Libraries
pip install streamlit pandas numpy scikit-learn joblib gtts

### Run the Application
streamlit run app.py

### Open in Browser


# 📂 Project Structure

FinTrust-AI
│
├── app.py
├── loan_model.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md


---

# 🎓 Learning Outcomes

This project demonstrates:

- Practical implementation of Machine Learning
- Model training and evaluation
- Real-time AI deployment
- Financial risk analysis
- Application of AI in banking systems

# 📌 Conclusion

FinTrust AI demonstrates how Artificial Intelligence can modernize the traditional loan approval process. By integrating machine learning with a web application and voice assistance, the system provides fast, accurate, and accessible loan evaluation for users.


# 👩‍💻 Author

**Snehitha Chintham**  
Artificial Intelligence Student  
Anurag University



### 8️⃣ Model Saving
The trained model was saved using Joblib as:
