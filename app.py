from google import genai
import os

# Put your NEW API key here
API_KEY = "AIzaSyAjbURRK2Aapv6NMSzWnAWR-o_LNtle7wE"

client = genai.Client(api_key=API_KEY)

print("===== AI News Intelligence System =====\n")

news_text = input("Paste the news article here:\n")

prompt = f"""
Analyze the following news article and provide:

1. Sentiment (Positive / Negative / Neutral)
2. Category
3. Short Summary
4. 5 Keywords

Article:
{news_text}
"""

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt
)

print("\n===== AI Analysis Result =====\n")
print(response.text)
