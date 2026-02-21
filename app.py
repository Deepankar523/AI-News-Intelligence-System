import streamlit as st
from google import genai

if "GEMINI_API_KEY" not in st.secrets:
    st.error("API Key not found in Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=st.secrets["AIzaSyAjbURRK2Aapv6NMSzWnAWR-o_LNtle7wE"])

st.title("📰 AI News Intelligence System")

news_text = st.text_area("Paste News Article Here")

if news_text:
    prompt = f"""
    Analyze the following news article and provide:

    1. Sentiment (Positive/Negative/Neutral)
    2. Category
    3. Summary
    4. 5 Keywords

    Article:
    {news_text}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    st.subheader("AI Analysis Result")
    st.write(response.text)

