# main.py

import streamlit as st
import os

# Import your custom modules
from speech_to_text import listen_once
from nlp_engine import ask_llm
from text_to_speech import speak
from pdf_tools import extract_text_from_pdf, summarize_text
from image_gen import generate_image

# Set Streamlit page configuration
st.set_page_config(page_title="AI Wearable/Static Assistant")

st.markdown(
    "<h1 style='text-align: center;'>🤖 AI Wearable / Static Assistant</h1>",
    unsafe_allow_html=True,
)

# --- Modes ---
mode = st.radio("Choose your mode:", ["Text Chat", "Voice Command"])

# --- Text Chat Mode ---
if mode == "Text Chat":
    user_input = st.text_input("Ask me anything:")
    if st.button("Submit"):
        if user_input:
            with st.spinner("Thinking..."):
                answer = ask_llm(user_input)
            st.write(f"**Assistant:** {answer}")
            # Optional speech reply
            if st.checkbox("Speak the answer"):
                speak(answer)

# --- Voice Command Mode ---
elif mode == "Voice Command":
    if st.button("Start Listening"):
        recognized_text = listen_once()
        if recognized_text:
            st.write(f"**You said:** {recognized_text}")
            with st.spinner("Thinking..."):
                answer = ask_llm(recognized_text)
            st.write(f"**Assistant:** {answer}")
            if st.checkbox("Speak the answer"):
                speak(answer)
        else:
            st.warning("No speech recognized.")

# --- PDF Summarization ---
st.header("📄 PDF Summarization")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.text_area("Document Text", text, height=200)

    if st.button("Summarize PDF"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(ask_llm, text)
        st.subheader("Summary:")
        st.write(summary)
        if st.checkbox("Speak the summary"):
            speak(summary)

# --- Image Generation ---
st.header("🎨 Generate Image from Prompt")

prompt = st.text_input("Enter your image description (or speak it!)")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            image_url = generate_image(prompt)
        st.image(image_url, caption="AI-Generated Image")
        st.write(f"[View Image]({image_url})")
    else:
        st.warning("Please enter a text prompt.")

# --- Speech-to-Image ---
if st.checkbox("Use voice for image prompt"):
    if st.button("Speak Prompt"):
        spoken_prompt = listen_once()
        if spoken_prompt:
            st.write(f"You said: {spoken_prompt}")
            with st.spinner("Generating image..."):
                image_url = generate_image(spoken_prompt)
            st.image(image_url, caption="AI-Generated Image")
            st.write(f"[View Image]({image_url})")
        else:
            st.warning("No speech recognized.")

st.write("---")
st.caption("Built with Python, Streamlit, OpenAI, and LangChain.")
