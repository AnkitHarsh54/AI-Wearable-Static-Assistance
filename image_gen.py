# image_gen.py

import os
from openai import OpenAI, error
import streamlit as st
import traceback

def generate_image(prompt: str) -> str:
    """
    Generates an image from text using OpenAI's DALL·E 3 API.
    Returns a URL to the generated image or None if generation fails.
    """

    # Check for empty prompt
    if not prompt or not prompt.strip():
        st.warning("Please enter an image prompt. It cannot be empty.")
        return None

    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI(api_key=api_key)

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt.strip(),
            n=1,
            size="1024x1024"
        )

        if response and response.data and response.data[0].url:
            return response.data[0].url
        else:
            st.error("Image generation failed: No URL returned.")
            return None

    except error.OpenAIError as e:
        st.error(f"OpenAI API error: {str(e)}")
        tb = traceback.format_exc()
        st.code(tb)
        return None

    except Exception as e:
        st.error(f"Unexpected error during image generation: {str(e)}")
        tb = traceback.format_exc()
        st.code(tb)
        return None
