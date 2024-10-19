import streamlit as st

# Define a function to estimate HbA1c based on average blood glucose
def estimate_hba1c(avg_glucose):
    return (avg_glucose + 46.7) / 28.7

# Define a function to provide health advice based on glucose levels
def health_advice(glucose_level, time_of_day):
    if time_of_day == 'Fasting':
        if glucose_level < 70:
            return "⚠️ **Low blood glucose (hypoglycemia)**: You may feel shaky or dizzy. Please consult your doctor."
        elif 70 <= glucose_level <= 99:
            return "✅ **Normal fasting glucose level**: Keep up the good work with your healthy lifestyle."
        elif 100 <= glucose_level <= 125:
            return "🟡 **Prediabetes range**: Consider making changes to your diet and increasing physical activity."
        else:
            return "❗ **High blood glucose (diabetes)**: Please consult a healthcare provider for further evaluation."
    elif time_of_day == 'Postprandial (after meal)':
        if glucose_level < 140:
            return "✅ **Normal postprandial glucose level**: This is a healthy range after meals."
        elif 140 <= glucose_level <= 199:
            return "🟡 **Prediabetes range**: Monitor your meals and consider lifestyle changes."
        else:
            return "❗ **High blood glucose (diabetes)**: It is important to consult your doctor."
    else:
        return "⚠️ Invalid time of day."

# Streamlit App UI
st.title("🩸 Blood Glucose & HbA1c Health Advisor")

st.markdown("""
Welcome to the **Blood Glucose & HbA1c Estimator**!  
This app helps you assess your blood glucose levels, provides health advice based on your input, and estimates your HbA1c—a key indicator of long-term blood sugar control.  
Let's get started!  
""")

# Create columns for better layout
col1, col2 = st.columns(2)

# Collect user input in the first column
with col1:
    st.header("🔢 Input Your Blood Glucose Data")
    
    glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0, step=1)
    time_of_day = st.selectbox("When was this measurement taken?", ['Fasting', 'Postprandial (after meal)'])
    
    # Detailed explanation of blood glucose readings
    st.markdown("""
    **Fasting**: Blood glucose level measured after 8+ hours without food.  
    **Postprandial**: Blood glucose level measured 2 hours after eating a meal.  
    """)

# Provide health advice based on glucose level in the second column
with col2:
    if glucose_level:
        st.header("📊 Health Advice")
        advice = health_advice(glucose_level, time_of_day)
        st.write(advice)

# Additional input and calculations
st.header("🔍 Estimate Your HbA1c")

st.markdown("""
The HbA1c test measures your average blood glucose levels over the past 2-3 months.  
If you know your average blood glucose level, enter it below to estimate your HbA1c:
""")

avg_glucose = st.number_input("Enter your average blood glucose level (mg/dL):", min_value=0, step=1)

# Calculate and display HbA1c
if avg_glucose:
    hba1c = estimate_hba1c(avg_glucose)
    st.write(f"🧮 **Your estimated HbA1c is:** `{hba1c:.2f}%`")
    if hba1c < 5.7:
        st.success("Your HbA1c is in the **normal range**. Keep maintaining a healthy lifestyle!")
    elif 5.7 <= hba1c < 6.5:
        st.warning("Your HbA1c indicates **prediabetes**. It's time to take action with healthier habits!")
    else:
        st.error("Your HbA1c indicates **diabetes**. Please consult a healthcare provider for further advice.")

# Conclusion with footer
st.markdown("---")
st.markdown("""
*Disclaimer*: The health advice and HbA1c estimation provided here are for informational purposes only.  
Always consult a healthcare provider for personalized medical advice and diagnosis.
""")

st.markdown("""
💡 **Tip**: To maintain healthy blood glucose levels, consider regular exercise, a balanced diet, and routine checkups with your doctor.
""")
