# 🤖 AI Wearable / Static Assistant

Your all-in-one AI-powered assistant for:

- 💬 Text-based conversation (powered by Google Gemini)
- 🎤 Voice commands with speech-to-text
- 📄 PDF text extraction and summarization

Beautifully built using **Streamlit** with sleek UI styling and animations.

---

## 🌟 Features

### 💬 Text Chat

- Chat directly with Google Gemini.
- Supports free-form queries and document summaries.
- Optionally speak out answers using text-to-speech (pyttsx3).

---

### 🎤 Voice Command

- Upload audio recordings (WAV, MP3).
- Transcribes speech into text via AssemblyAI.
- Gets smart responses from Gemini based on your spoken question.
- Optional audio playback of responses.

---

### 📄 PDF Summarization

- Upload any PDF document.
- Extracts raw text using PyMuPDF.
- Summarizes content via Gemini.
- Speak summaries for easy listening.

---

## ⚙️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
    - Custom CSS styling
    - Responsive UI
    - Lottie animations
- **LLM Backend:**
    - Google Gemini (via google-generativeai)
- **Voice Processing:**
    - AssemblyAI for speech-to-text
    - pyttsx3 for text-to-speech
    - SpeechRecognition & pydub for audio handling
- **PDF Tools:**
    - PyMuPDF for PDF text extraction
- **Others:**
    - gdown for file downloads (if needed)
    - dotenv & Streamlit Secrets for environment variables

---

## 🖼️ Screenshots

Here’s a preview of the AI Wearable / Static Assistant UI:

<img src="https://github.com/user-attachments/assets/d2fd35ba-5870-46e1-b6d6-971e8577bd77" style="width: 500px; height: auto;" />

