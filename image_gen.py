# main.py

import streamlit as st
from nlp_engine import ask_llm
from pdf_tools import extract_text_from_pdf, summarize_text
from image_gen import generate_image
from speech_to_text import transcribe_audio
from text_to_speech import speak
from streamlit_lottie import st_lottie
import requests

# Helper to load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

mic_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_q8qssqgz.json")

# Hero background image URL (Unsplash)
hero_image_url = "https://images.unsplash.com/photo-1610484826967-f3e9b44f37dc?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80"

# Tab-specific images
images = {
    "chat": "https://images.unsplash.com/photo-1639755378189-7f1efc2f910d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1170&q=80",
    "voice": "https://images.unsplash.com/photo-1593784990066-d91e9dc447f2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1170&q=80",
    "pdf": "https://images.unsplash.com/photo-1648380062154-cb3f423a074c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80",
    "image_gen": "https://images.unsplash.com/photo-1617355607457-482f68bb7c85?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80"
}

# Page Config
st.set_page_config(
    page_title="AI Wearable / Static Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS Styling
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
        background-color: #0c0c1d;
        color: #f2f2f2;
    }}

    .stButton > button {{
        background-color: #4A90E2;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: #357ABD;
    }}

    .hero {{
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.7)), 
                    url('{hero_image_url}');
        background-size: cover;
        background-position: center;
        border-radius: 15px;
        padding: 3rem;
        text-align: center;
        margin-bottom: 3rem;
    }}

    .hero h1 {{
        color: white;
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }}

    .hero p {{
        color: #e0e0e0;
        font-size: 1.2rem;
    }}

    .tab-image {{
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
        max-width: 100%;
    }}

    .custom-card {{
        background: #1e1e2f;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
    }}
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h1>🤖 AI Wearable / Static Assistant</h1>
        <p>Your smart AI buddy for text, voice, PDF, and AI-generated art.</p>
    </div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "💬 Text Chat",
    "🎤 Voice Command",
    "📄 PDF Summarization",
    "🎨 Image Generation"
])

# --- Text Chat ---
with tab1:
    st.image(images["chat"], use_column_width=True, caption="Chat with Gemini", output_format="auto", class_="tab-image")
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
    st.image(images["voice"], use_column_width=True, caption="Voice Command", output_format="auto", class_="tab-image")
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
    st.image(images["pdf"], use_column_width=True, caption="AI & Document Summarization", output_format="auto", class_="tab-image")
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

# --- Image Generation ---
with tab4:
    st.image(images["image_gen"], use_column_width=True, caption="AI Art Generator", output_format="auto", class_="tab-image")
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🎨 Image Generation")
    prompt = st.text_input("Enter your image prompt:", placeholder="e.g. A futuristic city skyline at sunset")
    if st.button("Generate Image"):
        with st.spinner("Creating your artwork..."):
            image_url = generate_image(prompt)
        if image_url:
            st.image(image_url, caption="AI-Generated Image", use_column_width=True)
        else:
            st.warning("Image generation failed. Please try again.")
    st.markdown('</div>', unsafe_allow_html=True)
