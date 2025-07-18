import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

def parse_gemini_response(text: str) -> dict:
    lines = text.strip().splitlines()
    data = {"verdict": "", "reasoning": "", "suggestion": ""}
    for line in lines:
        if "verdict" in line.lower():
            data["verdict"] = line.split(":")[1].strip()
        elif "reasoning" in line.lower():
            data["reasoning"] = line.split(":")[1].strip()
        elif "suggestion" in line.lower():
            data["suggestion"] = line.split(":")[1].strip()
    return data

def analyze_content(user_input: str) -> dict:
    prompt = f"""
Analyze the following content and determine if it's a phishing message.

Content:
\"\"\"{user_input}\"\"\"

Return:
1. Verdict: "Safe", "Neutral", or "Likely Phishing"
2. Reasoning: Clear explanation for the verdict
3. Suggestion: What the user should do next
"""
    try:
        response=model.generate_content(prompt)
        return parse_gemini_response(response.text)
    except Exception as e:
        return {"error":str(e)}