import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")

st.title("📰 AI News Intelligence System")

news_text = st.text_area("Paste News Article Here")

if news_text:
    prompt = f"""
    Analyze the following news article and provide:

    1. Sentiment (Positive/Negative/Neutral)
    2. Category
    3. Short Summary
    4. 5 Keywords

    Article:
    {news_text}
    """

    response = model.generate_content(prompt)

    st.subheader("AI Analysis Result")
    st.write(response.text)
