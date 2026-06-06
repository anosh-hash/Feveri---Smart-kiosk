# 🌡️ Feverix - Smart Healthcare Kiosk

A smart fever screening kiosk built with Arduino + Python that detects 
fever, assesses symptom-based risk levels, and provides instant 
medical guidance — without needing a doctor.

Built as part of **Portal of Innovations Hackathon** by Team **MediPulse**.

---

## 💡 Problem It Solves
People ignore fever symptoms, delay doctor visits, and lack awareness 
about severity. No public kiosk system exists for quick, reliable 
fever screening — leading to late treatment and unnecessary hospital 
overcrowding.

---

## ⚙️ Tech Stack
| Layer | Tools Used |
|-------|-----------|
| Hardware | Arduino Uno/Nano, MLX90614 IR Sensor, LCD Display, Buzzer |
| Programming | C/C++ (Arduino IDE), Python |
| Simulation | Tinkercad |
| Data | Custom fever symptom dataset (.xlsx) |

---

## 🔑 Key Features
- 🌡️ Real-time contactless temperature monitoring via MLX90614 sensor
- 📊 Symptom-based risk classification: Low / Medium / High / Critical
- 🚨 Red flag detection with buzzer alert for critical fever cases
- 💊 Smart medical advice and basic medicine suggestions
- 📈 Fever history tracking and trend visualization
- 🏥 Nearby hospital guidance for emergency support
- 📱 QR code to use on mobile

---

## 🔄 How It Works
1. MLX90614 sensor reads body temperature via I2C communication
2. Arduino converts data to Celsius/Fahrenheit
3. Compares with WHO fever guidelines
4. Classifies risk level and triggers alert if threshold exceeded
5. Displays result + advice on LCD screen

---

## 🎯 Impact
- Reduces unnecessary hospital visits by filtering minor cases
- Provides early warning for severe conditions
- Useful for rural areas, schools, malls, airports, and hospitals
- Scalable B2B model for healthcare institutions

---

## 👩‍💻 Contributors
- Anoshka Roshini S — [@anosh-hash](https://github.com/anosh-hash)

---

## 🏆 Built At
Portal of Innovations Hackathon | Domain: Embedded Systems & Healthcare Technology
