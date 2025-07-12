# 🤖 OmniAI Assistant

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
    - gdown for file downloads
    - Streamlit Secrets for environment variables

---

## 🖼️ Screenshots

Here’s a preview of the AI Wearable / Static Assistant UI:
<img width="700" height="450" alt="image" src="https://github.com/user-attachments/assets/c6a5321f-0205-4e62-8b09-2170a3a0a5d2" />


