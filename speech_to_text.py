import assemblyai as aai
import streamlit as st
import tempfile

api_key = st.secrets["ASSEMBLYAI_API_KEY"]
aai.settings.api_key = api_key

def transcribe_audio(uploaded_file) -> str:
    """
    Transcribe uploaded audio file using AssemblyAI.
    """
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(tmp_path)

        return transcript.text

    except Exception as e:
        st.error(f"Transcription error: {e}")
        return "Sorry, speech-to-text failed."
