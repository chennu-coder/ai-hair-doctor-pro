import streamlit as st
from ai_agent import run_agent

# Page config
st.set_page_config(
    page_title="AI Hair Doctor Pro",
    page_icon="💇‍♂️",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    color: #4ade80;
}

.block-container {
    padding-top: 2rem;
}

.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

.stButton>button {
    background: linear-gradient(90deg, #22c55e, #4ade80);
    color: black;
    border-radius: 10px;
    font-weight: bold;
    height: 3em;
    width: 100%;
}

.result-box {
    background: #020617;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #4ade80;
    margin-top: 20px;
}

.sidebar .sidebar-content {
    background-color: #020617;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("💇‍♂️ AI Hair Doctor")
    st.markdown("### Smart Hair Analysis")
    st.markdown("---")

    st.info("💡 Get personalized hair fall solutions using AI")

    st.markdown("### 📊 Features")
    st.markdown("""
    - Hair fall detection  
    - Diet recommendations  
    - AI insights  
    - Health score  
    """)

# ---------- HERO ----------
st.markdown("""
<h1 style='text-align:center;'>AI Hair Doctor Pro 💇‍♂️</h1>
<p style='text-align:center; font-size:18px; color:gray;'>
Understand your hair fall & fix it with AI-powered insights
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- MAIN LAYOUT ----------
col1, col2 = st.columns([1, 1])

# ---------- INPUT SECTION ----------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧾 Enter Your Details")

    age = st.number_input("Age", 18, 60, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    hair_loss = st.selectbox("Hair Loss Level", ["Low", "Medium", "High"])
    diet = st.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian"])
    stress = st.slider("Stress Level", 1, 10)

    analyze = st.button("🚀 Analyze My Hair")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RESULT SECTION ----------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Analysis Result")

    if analyze:
        with st.spinner("🧠 AI is analyzing your hair condition..."):
            result = run_agent(age, gender, hair_loss, diet, stress)

        # Fake score logic (you can improve later)
        score = 100 - (stress * 5)

        st.metric("Hair Health Score", f"{score}%", "Needs Attention" if score < 70 else "Good")

        st.progress(score)

        st.markdown(f"""
        <div class="result-box">
        <h3>🧠 AI Diagnosis</h3>
        <p>{result}</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("Fill details and click **Analyze** to see results")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Built with ❤️ using AI | Your Personal Hair Health Assistant
</p>
""", unsafe_allow_html=True)
