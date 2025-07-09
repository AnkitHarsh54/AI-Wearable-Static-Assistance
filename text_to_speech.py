# text_to_speech.py

from huggingface_hub import InferenceClient
import streamlit as st

def speak(text):
    hf_token = st.secrets["HF_TOKEN"]
    model_id = "facebook/fastspeech2-en-ljspeech"

    client = InferenceClient(model=model_id, token=hf_token)

    # Generate speech audio (returns bytes)
    audio_bytes = client.text_to_speech(text)

    # Streamlit playback
    st.audio(audio_bytes, format="audio/wav")
