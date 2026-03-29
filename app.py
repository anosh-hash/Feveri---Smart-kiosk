import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Feverix Kiosk",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# LANGUAGE SELECT
# -----------------------------
lang = st.sidebar.selectbox("🌐 Select Language", ["English", "தமிழ்", "हिन्दी"])

# -----------------------------
# TEXT DICTIONARY
# -----------------------------
texts = {
    "English": {
        "title": "🩺 Feverix Smart Kiosk",
        "patient_details": "📋 Patient Details",
        "name": "👤 Name",
        "age": "🎂 Age",
        "temperature": "🌡️ Temperature (°F)",
        "days": "📅 Fever Days",
        "symptoms": "🤒 Symptoms",
        "headache": "🤕 Headache",
        "fatigue": "😴 Fatigue",
        "body_ache": "💪 Body Ache",
        "check_status": "🔍 CHECK HEALTH STATUS",
        "fever": "🌡️ Fever",
        "risk": "⚖️ Risk",
        "red_flag": "🚨 RED FLAG",
        "yes": "YES",
        "no": "NO",
        "fever_trend": "📊 Fever Trend",
        "nearby_hospitals": "📍 Nearby Hospitals",
        "find_hospitals": "Find Nearby Hospitals",
        "reset": "🔄 Reset",
        "footer": "🏥 Smart Health Kiosk"
    },
    "தமிழ்": {
        "title": "🩺 ஃபீவரிக்ஸ் ஸ்மார்ட் கியோஸ்க்",
        "patient_details": "📋 நோயாளி விவரங்கள்",
        "name": "👤 பெயர்",
        "age": "🎂 வயது",
        "temperature": "🌡️ உடல் வெப்பம் (°F)",
        "days": "📅 காய்ச்சல் நாட்கள்",
        "symptoms": "🤒 அறிகுறிகள்",
        "headache": "🤕 தலைவலி",
        "fatigue": "😴 சோர்வு",
        "body_ache": "💪 உடல் வலி",
        "check_status": "🔍 சுகாதார நிலை பரிசோதனை",
        "fever": "🌡️ காய்ச்சல்",
        "risk": "⚖️ அபாயம்",
        "red_flag": "🚨 சிவப்பு கொடி",
        "yes": "ஆம்",
        "no": "இல்லை",
        "fever_trend": "📊 காய்ச்சல் வரிசை",
        "nearby_hospitals": "📍 அருகிலுள்ள மருத்துவமனைகள்",
        "find_hospitals": "மருத்துவமனைகள் கண்டறி",
        "reset": "🔄 மீட்டமை",
        "footer": "🏥 ஸ்மார்ட் ஹெல்த் கியோஸ்க்"
    },
    "हिन्दी": {
        "title": "🩺 फीवरिक्स स्मार्ट कियोस्क",
        "patient_details": "📋 रोगी विवरण",
        "name": "👤 नाम",
        "age": "🎂 उम्र",
        "temperature": "🌡️ तापमान (°F)",
        "days": "📅 बुखार के दिन",
        "symptoms": "🤒 लक्षण",
        "headache": "🤕 सिर दर्द",
        "fatigue": "😴 थकान",
        "body_ache": "💪 बदन दर्द",
        "check_status": "🔍 स्वास्थ्य स्थिति जाँचें",
        "fever": "🌡️ बुखार",
        "risk": "⚖️ जोखिम",
        "red_flag": "🚨 लाल झंडा",
        "yes": "हाँ",
        "no": "नहीं",
        "fever_trend": "📊 बुखार का रुझान",
        "nearby_hospitals": "📍 नजदीकी अस्पताल",
        "find_hospitals": "अस्पताल खोजें",
        "reset": "🔄 रीसेट",
        "footer": "🏥 स्मार्ट हेल्थ कियोस्क"
    }
}

t = texts[lang]

# -----------------------------
# 🔥 ULTRA CLEAR CSS
# -----------------------------
st.markdown("""
<style>
.big-title { text-align: center; font-size: 48px; font-weight: bold; color: #0B3C5D; }
.card { padding: 30px; border-radius: 18px; text-align: center; background-color: #FFFFFF; border: 3px solid #000; }
.label { font-size: 20px; color: #000; font-weight: bold; }
.fever-text { color: #0066FF; font-size: 36px; font-weight: bold; }
.low { color: #00C853; font-size: 36px; font-weight: bold; }
.medium { color: #FF8F00; font-size: 36px; font-weight: bold; }
.high { color: #FF3D00; font-size: 36px; font-weight: bold; }
.critical { color: #FFFFFF; font-size: 36px; font-weight: bold; }
.red-yes { color: #FFFFFF; font-size: 36px; font-weight: bold; }
.red-no { color: #00C853; font-size: 36px; font-weight: bold; }
.alert-box { background-color: #FF0000 !important; color: white !important; }
button[kind="primary"] { height: 75px; font-size: 24px; border-radius: 14px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("final_smart_fever_dataset.xlsx")
    df.columns = df.columns.str.strip().str.lower()
    return df

df = load_data()

# -----------------------------
# SESSION
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# TITLE
# -----------------------------
st.markdown(f"<div class='big-title'>{t['title']}</div>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# INPUT
# -----------------------------
st.markdown(f"### {t['patient_details']}")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input(t["name"])
    age = st.number_input(t["age"], 0, 100)

with col2:
    temperature = st.number_input(t["temperature"], 95.0, 110.0)
    days = st.number_input(t["days"], 0, 10)

# -----------------------------
# SYMPTOMS
# -----------------------------
st.markdown(f"### {t['symptoms']}")
c1, c2, c3 = st.columns(3)
with c1: headache = st.checkbox(t["headache"])
with c2: fatigue = st.checkbox(t["fatigue"])
with c3: body_ache = st.checkbox(t["body_ache"])

st.markdown("---")

# -----------------------------
# MAIN BUTTON
# -----------------------------
if st.button(t["check_status"], use_container_width=True):

    score = [headache, fatigue, body_ache].count(True)

    # Fever
    if temperature <= 98.6: fever = "normal"
    elif temperature < 100: fever = "mild"
    elif temperature < 102: fever = "moderate"
    else: fever = "high"

    # Risk
    if score == 0: risk = "low"
    elif score == 1: risk = "medium"
    else: risk = "high"

    # Red Flag
    red_flag = "Yes" if temperature > 103 or days > 5 else "No"
    if red_flag == "Yes": risk = "critical"

    # Save history
    st.session_state.history.append({
        "Time": datetime.now().strftime("%H:%M"),
        "Temp": temperature
    })

    # -----------------------------
    # RESULT UI
    # -----------------------------
    st.markdown("## 📊 Result")
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"<div class='card'><div class='label'>{t['fever']}</div><div class='fever-text'>{fever.upper()}</div></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='card'><div class='label'>{t['risk']}</div><div class='{risk}'>{risk.upper()}</div></div>", unsafe_allow_html=True)

    if red_flag == "Yes":
        col3.markdown(f"<div class='card alert-box'><div class='label'>{t['red_flag']}</div><div class='red-yes'>{t['yes']}</div></div>", unsafe_allow_html=True)
    else:
        col3.markdown(f"<div class='card'><div class='label'>{t['red_flag']}</div><div class='red-no'>{t['no']}</div></div>", unsafe_allow_html=True)

# -----------------------------
# CHART
# -----------------------------
st.markdown("---")
st.subheader(t["fever_trend"])
if st.session_state.history:
    df_hist = pd.DataFrame(st.session_state.history)
    plt.figure()
    plt.plot(df_hist["Time"], df_hist["Temp"], marker='o')
    st.pyplot(plt)

# -----------------------------
# HOSPITAL
# -----------------------------
st.markdown("---")
st.subheader(t["nearby_hospitals"])
if st.button(t["find_hospitals"]):
    st.markdown("[🔗 Open in Google Maps](https://www.google.com/maps/search/hospitals/)")

# -----------------------------
# RESET
# -----------------------------
if st.button(t["reset"]):
    st.session_state.history = []
    st.rerun()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption(t["footer"])