# main.py

import streamlit as st
from nlp_engine import ask_llm
from pdf_tools import extract_text_from_pdf, summarize_text
from speech_to_text import transcribe_audio
from text_to_speech import speak
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation for fun!
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

mic_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_q8qssqgz.json")

# Page Config
st.set_page_config(
    page_title="AI Wearable / Static Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #f2f2f2;
        background-color: #0c0c1d;
    }

    .stButton > button {
        background-color: #4A90E2;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #357ABD;
    }

    .custom-card {
        background: #1e1e2f;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #4A90E2 0%, #357ABD 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 3rem;
    ">
        <h1 style="margin-bottom: 10px;">🤖 AI Wearable / Static Assistant</h1>
        <p style="font-size: 1.2rem;">
            Your all-in-one smart assistant for text, voice and PDFs.
        </p>
    </div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3= st.tabs([
    "💬 Text Chat",
    "🎤 Voice Command",
    "📄 PDF Summarization"
])

# --- Text Chat ---
with tab1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("💬 Text Chat with Gemini")
    user_input = st.text_input("Ask me anything:", placeholder="e.g. Summarize this article...")
    if st.button("Submit", key="chat_button"):
        with st.spinner("Gemini is thinking..."):
            answer = ask_llm(user_input)
        st.success(answer)
        if st.checkbox("🔊 Speak the answer"):
            speak(answer)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Voice Command ---
with tab2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🎤 Voice Command (AssemblyAI)")

    if mic_animation:
        st_lottie(mic_animation, height=200)

    uploaded_audio = st.file_uploader(
        "Upload audio file (.wav, .mp3)",
        type=["wav", "mp3"]
    )

    if uploaded_audio and st.button("Transcribe Audio"):
        with st.spinner("Transcribing and thinking..."):
            transcript = transcribe_audio(uploaded_audio)
            st.info(f"📝 You said: {transcript}")
            answer = ask_llm(transcript)
        st.success(answer)
        if st.checkbox("🔊 Speak the answer"):
            speak(answer)
    st.markdown('</div>', unsafe_allow_html=True)

# --- PDF Summarization ---
with tab3:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("📄 PDF Summarization")

    uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_pdf:
        text = extract_text_from_pdf(uploaded_pdf)
        st.text_area("📄 Extracted Text", text, height=250)

        if st.button("Summarize PDF"):
            with st.spinner("Summarizing your document..."):
                summary = summarize_text(ask_llm, text)
            st.success(summary)
            if st.checkbox("🔊 Speak the summary"):
                speak(summary)
    st.markdown('</div>', unsafe_allow_html=True)


