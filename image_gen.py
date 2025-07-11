# image_gen.py

import streamlit as st
import base64
import requests
import traceback

def generate_image(prompt: str) -> str:
    try:
        hf_token = st.secrets["HF_TOKEN"]
        model_id = "stabilityai/sd-turbo"

        url = f"https://api-inference.huggingface.co/models/{model_id}"
        headers = {
            "Authorization": f"Bearer {hf_token}"
        }
        payload = {
            "inputs": prompt
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        image_bytes = response.content
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        image_url = f"data:image/png;base64,{encoded_image}"

        return image_url

    except Exception as e:
        tb = traceback.format_exc()
        st.error(f"Image generation error: {e}")
        st.code(tb)
        return None
