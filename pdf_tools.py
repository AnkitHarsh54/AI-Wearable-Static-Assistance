# pdf_tools.py

import fitz  # PyMuPDF
from nlp_engine import ask_llm

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract text from PDF file using PyMuPDF.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text(llm_function, text: str) -> str:
    """
    Summarize given text via Gemini LLM.
    """
    prompt = f"Summarize the following document:\n\n{text}"
    return llm_function(prompt)
