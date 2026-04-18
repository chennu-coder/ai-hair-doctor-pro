import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from scoring import calculate_score
from analytics import generate_analytics
from report import generate_report
from memory_store import save_user

from dotenv import load_dotenv

# Load env (works locally only)
load_dotenv()

import os
print("DEBUG AI_AGENT KEY:", os.getenv("GOOGLE_API_KEY"))

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Fail fast (VERY IMPORTANT)
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Check .env or Streamlit Secrets")

# Initialize LLM with key explicitly
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

def run_agent(user_data, image_analysis):

    prompt = f"""
    You are a professional hair doctor.

    Patient details:
    {user_data}

    Image analysis:
    {image_analysis}

    Give diagnosis and treatment.
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    # 📊 Score
    score = calculate_score(user_data)

    # 📈 Analytics
    analytics = generate_analytics(score)

    # 🧾 Report
    report = generate_report(user_data, response.content, score, analytics)

    save_user("user1", report)

    return report, score, analytics
