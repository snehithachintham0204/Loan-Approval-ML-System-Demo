import streamlit as st
import joblib
import pandas as pd
from datetime import date
from gtts import gTTS
import uuid

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("loan_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="FinTrust AI", layout="wide")

# -------------------------------
# LANGUAGE SELECTION
# -------------------------------
language = st.sidebar.selectbox("🌍 Select Language", ["English", "Hindi", "Telugu"])
lang_code = {"English": "en", "Hindi": "hi", "Telugu": "te"}

# -------------------------------
# TRANSLATIONS (ALL FIELDS INCLUDED)
# -------------------------------
translations = {

"English": {
"title":"🏦 FinTrust AI – Intelligent Loan & Risk Decision Engine",
"evaluate":"Evaluate Loan Application",
"approved":"Loan Approved",
"rejected":"Loan Rejected",
"risk":"Risk Percentage",
"emi_details":"EMI & Repayment Details",
"emi_sentence":"Your monthly EMI is",
"total_interest":"Total Interest Payable",
"total_payment":"Total Payment Over Tenure",
"suggestion":"Financial Suggestion",
"loan_reason":"Reason for Taking Loan",

"full_name":"Full Name",
"email":"Email ID",
"mobile":"Mobile Number",
"dob":"Date of Birth",
"gender":"Gender",
"married":"Marital Status",
"dependents":"Dependents",
"education":"Education",
"employment":"Employment Type",
"income":"Monthly Income",
"co_income":"Co-applicant Income",
"existing_emi":"Existing EMI",
"loan_amount":"Loan Amount",
"loan_term":"Loan Term (Months)",
"interest_rate":"Interest Rate (%)",
"credit_history":"Credit History",
"property_area":"Property Area",

"emi_high":"EMI is high compared to income. Reduce loan or increase tenure.",
"emi_medium":"EMI is moderate. Plan your expenses carefully.",
"emi_low":"EMI is affordable."
},

"Hindi": {
"title":"🏦 फिनट्रस्ट एआई – बुद्धिमान ऋण निर्णय प्रणाली",
"evaluate":"ऋण आवेदन जांचें",
"approved":"ऋण स्वीकृत",
"rejected":"ऋण अस्वीकृत",
"risk":"जोखिम प्रतिशत",
"emi_details":"ईएमआई और पुनर्भुगतान विवरण",
"emi_sentence":"आपकी मासिक ईएमआई है",
"total_interest":"कुल ब्याज",
"total_payment":"कुल भुगतान",
"suggestion":"वित्तीय सुझाव",
"loan_reason":"ऋण लेने का कारण",

"full_name":"पूरा नाम",
"email":"ईमेल आईडी",
"mobile":"मोबाइल नंबर",
"dob":"जन्म तिथि",
"gender":"लिंग",
"married":"वैवाहिक स्थिति",
"dependents":"आश्रित",
"education":"शिक्षा",
"employment":"रोजगार प्रकार",
"income":"मासिक आय",
"co_income":"सह-आवेदक आय",
"existing_emi":"मौजूदा ईएमआई",
"loan_amount":"ऋण राशि",
"loan_term":"ऋण अवधि (महीने)",
"interest_rate":"ब्याज दर (%)",
"credit_history":"क्रेडिट इतिहास",
"property_area":"संपत्ति क्षेत्र",

"emi_high":"आपकी आय की तुलना में ईएमआई अधिक है। ऋण कम करें या अवधि बढ़ाएं।",
"emi_medium":"ईएमआई मध्यम है। खर्चों की सही योजना बनाएं।",
"emi_low":"ईएमआई आपकी आय के अनुसार उचित है।"
},

"Telugu": {
"title":"🏦 ఫిన్‌ట్రస్ట్ AI – స్మార్ట్ లోన్ నిర్ణయ వ్యవస్థ",
"evaluate":"రుణ దరఖాస్తు పరిశీలించండి",
"approved":"రుణం ఆమోదించబడింది",
"rejected":"రుణం తిరస్కరించబడింది",
"risk":"రిస్క్ శాతం",
"emi_details":"EMI & తిరిగి చెల్లింపు వివరాలు",
"emi_sentence":"మీ నెలవారీ EMI",
"total_interest":"మొత్తం వడ్డీ",
"total_payment":"మొత్తం చెల్లింపు",
"suggestion":"ఆర్థిక సూచన",
"loan_reason":"రుణం తీసుకునే కారణం",

"full_name":"పూర్తి పేరు",
"email":"ఈమెయిల్ ఐడి",
"mobile":"మొబైల్ నంబర్",
"dob":"పుట్టిన తేదీ",
"gender":"లింగం",
"married":"వివాహ స్థితి",
"dependents":"ఆధారపడిన వారు",
"education":"విద్య",
"employment":"ఉద్యోగ రకం",
"income":"నెలవారీ ఆదాయం",
"co_income":"సహ దరఖాస్తుదారు ఆదాయం",
"existing_emi":"ప్రస్తుత EMI",
"loan_amount":"రుణ మొత్తం",
"loan_term":"రుణ వ్యవధి (నెలలు)",
"interest_rate":"వడ్డీ రేటు (%)",
"credit_history":"క్రెడిట్ చరిత్ర",
"property_area":"ఆస్తి ప్రాంతం",

"emi_high":"మీ ఆదాయంతో పోలిస్తే EMI ఎక్కువగా ఉంది. రుణాన్ని తగ్గించండి లేదా వ్యవధిని పెంచండి.",
"emi_medium":"EMI మధ్యస్థంగా ఉంది. ఖర్చులను సరిగా ప్లాన్ చేయండి.",
"emi_low":"EMI మీ ఆదాయానికి అనుకూలంగా ఉంది."
}
}

T = translations[language]

# -------------------------------
# SPEAK FUNCTION
# -------------------------------
def speak(text):
    filename = f"voice_{uuid.uuid4()}.mp3"
    gTTS(text=text, lang=lang_code[language]).save(filename)
    st.audio(filename, autoplay=True)

# -------------------------------
# INSTRUCTOR FUNCTION
# -------------------------------
def instructor(label, field_type):
    if language == "English":
        sentence = f"Please {'select' if field_type=='select' else 'enter'} your {label}"
    elif language == "Hindi":
        sentence = f"कृपया अपना {label} {'चुनें' if field_type=='select' else 'दर्ज करें'}"
    else:
        sentence = f"దయచేసి మీ {label} {'ఎంచుకోండి' if field_type=='select' else 'నమోదు చేయండి'}"
    speak(sentence)

# -------------------------------
# HEADER
# -------------------------------
st.title(T["title"])
st.markdown("---")

# -------------------------------
# FIELD FUNCTION
# -------------------------------
def field(key, field_type="text", options=None):

    col1, col2 = st.columns([5,1])
    label = T[key]

    with col1:
        if field_type=="text":
            value = st.text_input(label)
        elif field_type=="number":
            value = st.number_input(label, min_value=0)
        elif field_type=="date":
            value = st.date_input(label, min_value=date(1950,1,1))
        elif field_type=="select":
            value = st.selectbox(label, options)

    with col2:
        if st.button("🔊", key=f"{key}_{field_type}"):
            instructor(label, field_type)

    return value

# -------------------------------
# FORM FIELDS
# -------------------------------
full_name = field("full_name")
email = field("email")
mobile = field("mobile")
dob = field("dob","date")
gender = field("gender","select",["Male","Female"])
married = field("married","select",["Yes","No"])
dependents = field("dependents","select",[0,1,2,3,4])
education = field("education","select",
    ["Not Educated","Less than 10th Class","High School",
     "Diploma","Undergraduate","Graduate","Postgraduate","Doctorate"])
employment_type = field("employment","select",
    ["Salaried","Self Employed","Business Owner",
     "Government Employee","Student","Unemployed"])
loan_reason = field("loan_reason","select",
    ["Home Purchase","Education","Medical Emergency",
     "Business Expansion","Vehicle","Personal","Others"])
income = field("income","number")
co_income = field("co_income","number")
existing_emi = field("existing_emi","number")
loan_amount = field("loan_amount","number")
loan_term = field("loan_term","number")
interest_rate = field("interest_rate","number")
credit_history = field("credit_history","select",[0,1])
property_area = field("property_area","select",["Urban","Semiurban","Rural","No Area"])

# -------------------------------
# EVALUATION
# -------------------------------
if st.button(T["evaluate"]):

    property_encoding = {"Urban":2,"Semiurban":1,"Rural":0,"No Area":-1}

    input_dict = {
        "Gender":1 if gender=="Male" else 0,
        "Married":1 if married=="Yes" else 0,
        "Dependents":dependents,
        "Education":3,
        "Self_Employed":1 if employment_type=="Self Employed" else 0,
        "ApplicantIncome":income,
        "CoapplicantIncome":co_income,
        "LoanAmount":loan_amount,
        "Loan_Amount_Term":loan_term,
        "Credit_History":credit_history,
        "Property_Area":property_encoding[property_area]
    }

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    risk_percentage = round((1 - probability) * 100, 2)

    st.markdown("---")

    if prediction == 1:
        st.success(T["approved"])
        st.write(T["risk"], ":", risk_percentage, "%")

        if loan_term <= 0:
            emi = 0
            total_interest = 0
            total_payment = 0
        else:
            if interest_rate == 0:
                emi = loan_amount / loan_term
                total_payment = loan_amount
                total_interest = 0
            else:
                r = interest_rate/(12*100)
                emi = (loan_amount*r*(1+r)**loan_term)/((1+r)**loan_term-1)
                total_payment = emi*loan_term
                total_interest = total_payment-loan_amount

        emi = round(emi,2)
        total_interest = round(total_interest,2)
        total_payment = round(total_payment,2)

        st.subheader(T["emi_details"])
        st.write(T["emi_sentence"], ":", emi)
        st.write(T["total_interest"], ":", total_interest)
        st.write(T["total_payment"], ":", total_payment)

        if income+co_income > 0:
            emi_ratio = emi/(income+co_income)
        else:
            emi_ratio = 1

        st.subheader(T["suggestion"])

        if emi_ratio>0.5:
            suggestion_text=T["emi_high"]
        elif emi_ratio>0.3:
            suggestion_text=T["emi_medium"]
        else:
            suggestion_text=T["emi_low"]

        st.write(suggestion_text)

        speak(f"{T['approved']}. {T['emi_sentence']} {emi}. {suggestion_text}")

    else:
        st.error(T["rejected"])
        st.write(T["risk"], ":", risk_percentage, "%")
        speak(f"{T['rejected']}. {T['risk']} {risk_percentage} percent.")

st.markdown("---")
st.markdown("© 2026 FinTrust AI")