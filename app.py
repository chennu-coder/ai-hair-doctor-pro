import streamlit as st
from PIL import Image
from ai_agent import run_agent
from image_analyzer import analyze_image

st.set_page_config(page_title="AI Hair Doctor Pro")

st.title("🧑‍⚕️ AI Hair Doctor (Pro)")

# STEP 1: USER INPUT
age = st.number_input("Age", 18, 60)
gender = st.selectbox("Gender", ["Male", "Female"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
drinking = st.selectbox("Drinking", ["No", "Yes"])
years = st.number_input("Hair fall since (years)", 0, 30)
problem = st.text_area("Describe your hair problem")

# STEP 2: IMAGE
file = st.file_uploader("Upload scalp image", type=["jpg", "png"])

image = None
if file:
    image = Image.open(file)
    st.image(image)

# STEP 3: RUN
if st.button("Analyze Now"):

    if not problem or not file:
        st.warning("Please fill all details + upload image")
    else:
        with st.spinner("Analyzing..."):

            image_analysis = analyze_image(image)

            user_data = {
                "age": age,
                "gender": gender,
                "smoking": smoking,
                "drinking": drinking,
                "years": years,
                "problem": problem
            }

            report, score, analytics = run_agent(user_data, image_analysis)

            # 📊 UI OUTPUT
            st.success("Analysis Complete")

            st.metric("Hair Score", f"{score}/100")
            st.metric("Risk Level", analytics["risk"])
            st.metric("Confidence", analytics["confidence"])

            st.progress(score / 100)

            st.markdown(report)
