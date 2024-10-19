import streamlit as st

# Define a function to estimate HbA1c based on average blood glucose
def estimate_hba1c(avg_glucose):
    return (avg_glucose + 46.7) / 28.7

# Define a function to provide health advice based on glucose levels
def health_advice(glucose_level, time_of_day):
    if time_of_day == 'Fasting':
        if glucose_level < 70:
            return "Low blood glucose (hypoglycemia). Please consult your doctor."
        elif 70 <= glucose_level <= 99:
            return "Normal fasting glucose level. Maintain a healthy lifestyle."
        elif 100 <= glucose_level <= 125:
            return "Prediabetes range. Consider improving diet and exercise."
        else:
            return "High blood glucose (diabetes). Please consult a healthcare provider."
    elif time_of_day == 'Postprandial (after meal)':
        if glucose_level < 140:
            return "Normal postprandial glucose level."
        elif 140 <= glucose_level <= 199:
            return "Prediabetes range. Watch your diet and consider exercise."
        else:
            return "High blood glucose (diabetes). Please consult your doctor."
    else:
        return "Invalid time of day."

# Streamlit App UI
st.title("Blood Glucose Level & HbA1c Estimator")

# User inputs
glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0, step=1)
time_of_day = st.selectbox("When was this measurement taken?", ['Fasting', 'Postprandial (after meal)'])
avg_glucose = st.number_input("Enter your average blood glucose level (mg/dL):", min_value=0, step=1)

# Provide health advice based on glucose level
if glucose_level:
    advice = health_advice(glucose_level, time_of_day)
    st.write("Health Advice: ", advice)

# Estimate HbA1c
if avg_glucose:
    hba1c = estimate_hba1c(avg_glucose)
    st.write(f"Your estimated HbA1c is: {hba1c:.2f}%")

# Footer
st.write("Note: The health advice and HbA1c estimation provided here are for informational purposes only. Please consult a healthcare provider for personalized medical advice.")
