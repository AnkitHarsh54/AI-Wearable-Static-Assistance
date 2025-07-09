
from huggingface_hub import InferenceClient
import streamlit as st

def speak(text):
    hf_token = st.secrets["HF_TOKEN"]
    model_id = "facebook/fastspeech2-en-ljspeech"

    client = InferenceClient(model=model_id, token=hf_token)

    audio_bytes = client.text_to_speech(text)

    st.audio(audio_bytes, format="audio/wav")
