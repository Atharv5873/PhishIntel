import re
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

def clean_gemini_output(text: str) -> str:
    return re.sub(r'\*\*', '', text).strip()

def parse_gemini_response(text: str) -> dict:
    data = {
        "verdict": "",
        "reasoning": "",
        "suggestion": ""
    }

    text = clean_gemini_output(text)
    sections = re.split(r'\n\d+\.\s+', text)

    for section in sections:
        lower_sec = section.lower()

        if lower_sec.startswith("verdict"):
            match = re.search(r'verdict\s*:\s*(.*)', section, re.IGNORECASE | re.DOTALL)
            if match:
                data["verdict"] = match.group(1).strip()
        elif lower_sec.startswith("reasoning"):
            match = re.search(r'reasoning\s*:\s*(.*)', section, re.IGNORECASE | re.DOTALL)
            if match:
                data["reasoning"] = match.group(1).strip()
        elif lower_sec.startswith("suggestion"):
            match = re.search(r'suggestion\s*:\s*(.*)', section, re.IGNORECASE | re.DOTALL)
            if match:
                data["suggestion"] = match.group(1).strip()

    if not data["verdict"]:
        data["verdict"] = "Verdict not found."
    if not data["reasoning"]:
        data["reasoning"] = "Reasoning not found."
    if not data["suggestion"]:
        data["suggestion"] = "Suggestion not found."

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
        response = model.generate_content(prompt)
        cleaned_text = clean_gemini_output(response.text)
        result = parse_gemini_response(cleaned_text)
        return result
    except Exception as e:
        return {"error": str(e)}
