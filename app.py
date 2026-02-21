import streamlit as st
import os
from google import genai

api_key = os.getenv("AIzaSyAjbURRK2Aapv6NMSzWnAWR-o_LNtle7wE")

if not api_key:
    st.error("API Key not loaded. Check Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("📰 AI News Intelligence System")

news_text = st.text_area("Paste News Article Here")

if news_text:
    prompt = f"""
    Analyze the following news article and provide:

    1. Sentiment
    2. Category
    3. Summary
    4. Keywords

    Article:
    {news_text}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    st.subheader("AI Analysis Result")
    st.write(response.text)
