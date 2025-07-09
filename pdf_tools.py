import fitz  

def extract_text_from_pdf(uploaded_file):
    
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def summarize_text(llm_func, text):
    summary_prompt = f"Summarize this text:\n{text}"
    summary = llm_func(summary_prompt)
    return summary
