# image_gen.py

import google.generativeai as genai
import streamlit as st
import base64
import traceback

def generate_image(prompt: str) -> str:
    try:
        # Get Gemini API Key
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("models/imagegeneration")

        response = model.generate_content(prompt)

        # Gemini returns base64-encoded image content
        image_data = response.text.strip().split(",")[-1]
        image_url = f"data:image/png;base64,{image_data}"

        return image_url

    except Exception as e:
        tb = traceback.format_exc()
        st.error(f"Image generation error: {e}")
        st.code(tb)
        return None
