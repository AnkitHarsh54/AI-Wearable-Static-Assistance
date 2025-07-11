#image_gen.py
from huggingface_hub import InferenceClient
import streamlit as st
import base64

def generate_image(prompt):
    hf_token = st.secrets["HF_TOKEN"]

   
    model_id = "stabilityai/stable-diffusion-2-1"

    client = InferenceClient(model=model_id, token=hf_token)

 
    image_bytes = client.text_to_image(
        prompt,
        guidance_scale=7.5,
        num_inference_steps=30,
        size=(512, 512)
    )


    encoded_image = base64.b64encode(image_bytes).decode("utf-8")


    image_url = f"data:image/png;base64,{encoded_image}"

    return image_url
