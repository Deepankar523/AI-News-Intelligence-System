import streamlit as st
import requests

API_KEY = st.secrets["GEMINI_API_KEY"]

st.title("📰 AI News Intelligence System")

news_text = st.text_area("Paste News Article Here")

if news_text:
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""
    Analyze the following news article and provide:

    1. Sentiment (Positive/Negative/Neutral)
    2. Category
    3. Short Summary
    4. 5 Keywords

    Article:
    {news_text}
    """

    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    if "candidates" in result:
        output = result["candidates"][0]["content"]["parts"][0]["text"]
        st.subheader("AI Analysis Result")
        st.write(output)
    else:
        st.error("API Error:")
        st.write(result)
