import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables (local only)
load_dotenv()

import os
print("DEBUG IMAGE_ANALYZER KEY:", os.getenv("GOOGLE_API_KEY"))

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Fail fast (VERY IMPORTANT)
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY is missing. Check .env or Streamlit Secrets")

# Configure Gemini
genai.configure(api_key=api_key)

# Use correct model (supports image + text)
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_image(image):
    prompt = """
    You are an expert hair and scalp specialist.

    Analyze the given scalp image and provide:

    1. Hair Density (Low / Medium / High)
    2. Bald Spots (Yes/No + severity)
    3. Scalp Condition (Healthy / Dry / Dandruff / Infection)
    4. Possible Issues (Hair fall, thinning, etc.)
    5. Confidence Score (0 to 1)

    Keep response structured and professional.
    """

    try:
        response = model.generate_content([prompt, image])
        return response.text

    except Exception as e:
        return f"❌ Image analysis failed: {str(e)}"
