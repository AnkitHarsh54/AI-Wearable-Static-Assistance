# main.py

import streamlit as st
from nlp_engine import ask_llm
from pdf_tools import extract_text_from_pdf, summarize_text
from image_gen import generate_image
from speech_to_text import transcribe_audio
from text_to_speech import speak

st.set_page_config(
    page_title="AI Wearable / Static Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Wearable / Static Assistant")

tab1, tab2, tab3, tab4 = st.tabs([
    "💬 Text Chat",
    "🎤 Voice Command",
    "📄 PDF Summarization",
    "🎨 Image Generation"
])

# --- Text Chat ---
with tab1:
    st.subheader("Text Chat with Gemini")
    user_input = st.text_input("Ask me anything:")
    if st.button("Submit", key="chat_button"):
        answer = ask_llm(user_input)
        st.success(answer)
        if st.checkbox("Speak the answer"):
            speak(answer)

# --- Voice Command ---
with tab2:
    st.subheader("Voice Command (AssemblyAI)")

    uploaded_audio = st.file_uploader(
        "Upload audio file (.wav)",
        type=["wav", "mp3"]
    )

    if uploaded_audio and st.button("Transcribe Audio"):
        transcript = transcribe_audio(uploaded_audio)
        st.info(f"You said: {transcript}")
        answer = ask_llm(transcript)
        st.success(answer)
        if st.checkbox("Speak the answer"):
            speak(answer)

# --- PDF Summarization ---
with tab3:
    st.subheader("PDF Summarization")
    uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")
    if uploaded_pdf:
        text = extract_text_from_pdf(uploaded_pdf)
        st.text_area("Extracted Text", text, height=200)

        if st.button("Summarize PDF"):
            summary = summarize_text(ask_llm, text)
            st.success(summary)
            if st.checkbox("Speak the summary"):
                speak(summary)

# --- Image Generation ---
with tab4:
    st.subheader("Image Generation")
    prompt = st.text_input("Enter your image prompt:")
    if st.button("Generate Image"):
        image_url = generate_image(prompt)
        if image_url:
            st.image(image_url, caption="AI-Generated Image")
        else:
            st.warning("Image generation failed.")
