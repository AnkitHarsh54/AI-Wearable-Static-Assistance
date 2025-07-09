
import streamlit as st
import os

# Import your custom modules
from speech_to_text import listen_once
from nlp_engine import ask_llm
from tts import speak
from pdf_tools import extract_text_from_pdf, summarize_text
from image_gen import generate_image

# Set page config
st.set_page_config(page_title="AI Wearable/Static Assistant")

st.title("🤖 AI Wearable / Static Assistant")

# --- Modes ---
mode = st.radio("Choose your mode:", ["Text Chat", "Voice Command"])

# --- Text Chat Mode ---
if mode == "Text Chat":
    user_input = st.text_input("Ask me anything:")
    if st.button("Submit"):
        if user_input:
            # LLM response
            answer = ask_llm(user_input)
            st.write(f"**Assistant:** {answer}")
            # Optional speech reply
            if st.checkbox("Speak the answer"):
                speak(answer)

# --- Voice Command Mode ---
elif mode == "Voice Command":
    if st.button("Start Listening"):
        # Convert speech → text
        recognized_text = listen_once()
        st.write(f"**You said:** {recognized_text}")

        if recognized_text:
            answer = ask_llm(recognized_text)
            st.write(f"**Assistant:** {answer}")
            if st.checkbox("Speak the answer"):
                speak(answer)

# --- PDF Summarization ---
st.header("📄 PDF Summarization")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text:")
    st.text_area("Document Text", text, height=200)

    if st.button("Summarize PDF"):
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
        image_url = generate_image(prompt)
        st.image(image_url, caption="AI-Generated Image")
        st.write(f"[View Image]({image_url})")
    else:
        st.warning("Please enter a text prompt.")

# Optional: speech-to-image
if st.checkbox("Use voice for image prompt"):
    if st.button("Speak Prompt"):
        spoken_prompt = listen_once()
        st.write(f"You said: {spoken_prompt}")
        if spoken_prompt:
            image_url = generate_image(spoken_prompt)
            st.image(image_url, caption="AI-Generated Image")
            st.write(f"[View Image]({image_url})")

st.write("---")
st.caption("Built with Python, Streamlit, OpenAI, and LangChain.")
