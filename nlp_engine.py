import google.generativeai as genai
import streamlit as st

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def ask_llm(prompt_text: str) -> str:
    """
    Query Gemini LLM with the given prompt text.
    """
    if not prompt_text.strip():
        return "Please enter a question."

    try:
        response = model.generate_content(prompt_text)
        return response.text

    except Exception as e:
        st.error(f"LLM error: {e}")
        return "Sorry, there was an error talking to the AI model."
