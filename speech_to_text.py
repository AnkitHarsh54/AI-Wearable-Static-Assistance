import speech_recognition as sr
import streamlit as st

def listen_once():
    """
    Listens to microphone input and converts speech to text
    using Google Web Speech API via the SpeechRecognition library.
    """

    recognizer = sr.Recognizer()

    st.info("Listening... please speak into your microphone.")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    try:

        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.warning("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
