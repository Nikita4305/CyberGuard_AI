"""
Gemini Security Analysis Agent
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class GeminiSecurityAgent:

    def __init__(self):
        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def analyze(self, incident):

        prompt = f"""
You are an expert cybersecurity incident analyst.

Analyze the following security incident.

Return:
1. Attack Type
2. Severity
3. Confidence Score (0-100)
4. Risk Assessment
5. Recommended Actions

Incident:
{incident}
"""

        response = self.model.generate_content(
            prompt
        )

        return response.text
