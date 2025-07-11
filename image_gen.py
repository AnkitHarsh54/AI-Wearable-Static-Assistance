# image_gen.py

import os
from openai import OpenAI
import streamlit as st
import traceback

def generate_image(prompt: str) -> str:
    """
    Generates an image from text using OpenAI's DALL·E 3 API.
    Returns a URL to the generated image.
    """
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI(api_key=api_key)

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return image_url

    except Exception as e:
        tb = traceback.format_exc()
        st.error(f"Image generation error: {e}")
        st.code(tb)
        return None
