from openai import OpenAI
import streamlit as st

client = OpenAI()

def speak(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
        format="wav",
    )
    
    audio_bytes = response.content
    
    # Streamlit playback
    st.audio(audio_bytes, format="audio/wav")
