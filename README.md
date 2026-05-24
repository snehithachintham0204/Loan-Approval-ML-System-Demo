# 🏦 FinTrust AI – Intelligent Loan & Risk Decision Engine

## 📌 Overview

FinTrust AI is an Artificial Intelligence based loan approval and risk assessment system that helps predict whether a loan will be approved or rejected based on financial and personal parameters.

The system uses Machine Learning algorithms to analyze loan data and provide instant predictions. It also calculates risk percentage, EMI, total repayment amount, and provides financial suggestions for improving loan eligibility.

This project demonstrates how Artificial Intelligence can be applied in banking systems to automate loan evaluation, reduce manual errors, and support faster decision-making.

---

# 🎯 Project Objectives

- Build a Machine Learning model to predict loan approval.
- Compare multiple ML algorithms and select the best performing model.
- Deploy the trained model into a real-time web application.
- Provide financial insights such as EMI calculation and risk analysis.
- Improve accessibility through multilingual voice assistance.

---

# ⚙️ Technologies Used

## 💻 Programming Language
- Python

## 🤖 Machine Learning Libraries
- Scikit-learn
- Pandas
- NumPy
- Joblib

## 📊 Models Implemented
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost
- AdaBoost *(Selected Final Model)*

## 🌐 Deployment
- Streamlit (Web Application)

## 🔊 Additional Libraries
- gTTS (Google Text-to-Speech)

---

# 📊 Machine Learning Methodology

## 1️⃣ Dataset Preparation

The loan dataset was loaded and prepared for training.

---

## 2️⃣ Data Preprocessing

The dataset was cleaned and processed by:

- Handling missing values
- Cleaning incorrect data
- Formatting dataset values properly

---

## 3️⃣ Feature Encoding

Categorical variables such as:

- Gender
- Education
- Property Area

were converted into numerical values so they could be used by machine learning algorithms.

---

## 4️⃣ Train-Test Split

The dataset was divided into:

- Training Data
- Testing Data

This helps evaluate the model on unseen data.

---

## 5️⃣ Model Training

Multiple machine learning algorithms were trained including:

- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost

---

## 6️⃣ Model Comparison

All models were evaluated using accuracy metrics and compared to identify the best performing algorithm.

---

## 7️⃣ Model Selection

AdaBoost achieved the best performance and was selected as the final deployed model.

---

## 8️⃣ Model Saving

The trained model was saved using Joblib as:

- `loan_model.pkl`
- `model_columns.pkl`

This allows the model to be reused without retraining.

---

# 🌐 Web Application Development

The trained machine learning model was integrated into a Streamlit web application.

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

- ✅ Loan Approved
- ❌ Loan Rejected

It also calculates:

- Risk Percentage
- Risk Level *(Low / Moderate / High)*

---

# 💰 EMI Calculation

If the loan is approved, the system calculates EMI using the standard banking formula.

## 📌 EMI Formula

```math
EMI = \frac{P \times r \times (1+r)^n}{(1+r)^n - 1}
```

### Where:
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

The application includes voice assistance using Google Text-to-Speech (gTTS).

## ✨ Features

- Voice instructions for each input field
- Voice output for results
- Multi-language support

## 🌍 Supported Languages

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

# 🚀 Installation & Running the Project

## 📌 Step 1: Clone or Download the Project

```bash
git clone https://github.com/your-username/FinTrust-AI.git
```

---

## 📌 Step 2: Open the Project Folder

```bash
cd FinTrust-AI
```

---

## 📌 Step 3: Open Command Prompt / Terminal

Open Command Prompt (Windows) or Terminal (Mac/Linux) inside the project folder.

---

## 📌 Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

This installs all required dependencies.

---

## 📌 Step 5: Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 📌 Step 6: Open the Application

After running the command, Streamlit generates a local URL similar to:

```bash
http://localhost:8501
```

Open the URL in your browser to use the application.

---

# 📂 Project Structure

```bash
FinTrust-AI/
│
├── app.py
├── loan_model.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md
```

---

# 📊 Model Performance Comparison

| Model | Purpose |
|-------|---------|
| Logistic Regression | Basic classification |
| Decision Tree | Rule-based prediction |
| Random Forest | Ensemble bagging method |
| Gradient Boosting | Sequential boosting |
| XGBoost | Optimized boosting |
| AdaBoost | Final selected model |

---

# 🎓 Learning Outcomes

This project demonstrates:

- Practical implementation of Machine Learning
- Model training and evaluation
- Real-time AI deployment
- Financial risk analysis
- Application of AI in banking systems
- Web application development using Streamlit
- Voice assistance integration

---

# 🔮 Future Enhancements

Future improvements can include:

- Real-time Banking API Integration
- Explainable AI (XAI)
- Fraud Detection System
- Cloud Deployment using AWS/Azure
- Database Integration
- Advanced Credit Score Analysis

---

# 📌 Conclusion

FinTrust AI demonstrates how Artificial Intelligence can modernize the traditional loan approval process. By integrating machine learning with a web application and multilingual voice assistance, the system provides fast, accurate, and accessible loan evaluation for users.

The project highlights the practical application of AI in banking systems for improving efficiency, reducing risk, and supporting smarter financial decisions.

---

# 👩‍💻 Author

## Snehitha Chintham
Artificial Intelligence Student  
Anurag University

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
