import google.generativeai as genai
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_image(image):
    prompt = """
    Analyze scalp image:
    - Hair density
    - Bald spots
    - Scalp condition
    """

    response = model.generate_content([prompt, image])
    return response.text