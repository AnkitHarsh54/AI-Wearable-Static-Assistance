import pyttsx3
import streamlit as st
import tempfile

def speak(text: str):
    """
    Generate audio from text using pyttsx3, and play in Streamlit.
    """
    try:
        engine = pyttsx3.init()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp_path = tmp.name
            engine.save_to_file(text, tmp_path)
            engine.runAndWait()

        audio_file = open(tmp_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

    except Exception as e:
        st.error(f"TTS error: {e}")
