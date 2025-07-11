import streamlit as st
from nlp_engine import ask_llm
from speech_to_text import listen_once
from text_to_speech import speak
from pdf_tools import extract_text_from_pdf, summarize_text
from image_gen import generate_image

st.set_page_config(
    page_title="AI Wearable Assistant",
    page_icon="🤖",
    layout="wide"
)

# Load custom CSS
with open(".streamlit/custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hero section
col1, col2 = st.columns([1, 5])

with col1:
    st.image("https://your-logo-url.png", width=80)

with col2:
    st.markdown("""
        <h1 style='color:#FF4B4B;margin-bottom:0;'>AI Wearable / Static Assistant</h1>
        <p style='color:gray;'>Powered by Gemini, AssemblyAI, Hugging Face</p>
    """, unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["💬 Text Chat", "🎤 Voice Command", "📄 PDF Summarization", "🎨 Image Generation"]
)

with tab1:
    st.subheader("Text Chat with Gemini")
    user_input = st.text_input("Ask something...")
    if st.button("Submit", key="submit_text"):
        answer = ask_llm(user_input)
        st.success(answer)

with tab2:
    st.subheader("Voice Command")
    if st.button("Start Listening"):
        transcript = listen_once()
        st.info(f"You said: {transcript}")

with tab3:
    st.subheader("PDF Summarization")
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text", text, height=200)
        if st.button("Summarize PDF"):
            summary = summarize_text(ask_llm, text)
            st.success(summary)

with tab4:
    st.subheader("Image Generation")
    prompt = st.text_input("Enter your image prompt:")
    if st.button("Generate Image"):
        url = generate_image(prompt)
        st.image(url, caption="AI-Generated Image")
