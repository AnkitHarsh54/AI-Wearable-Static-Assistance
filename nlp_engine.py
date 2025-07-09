# nlp_engine.py

import streamlit as st
from huggingface_hub import InferenceClient

def ask_llm(prompt_text):
    if not prompt_text.strip():
        return "Please enter a question."

    try:
        hf_token = st.secrets["HF_TOKEN"]
        
        # Example model - change to any you like!
        model_id = "google/flan-t5-base"
        
        client = InferenceClient(model=model_id, token=hf_token)
        result = client.text_generation(
            prompt_text,
            max_new_tokens=200,
        )
        return result
    except Exception as e:
        st.error(f"LLM error: {e}")
        return "Sorry, there was an error talking to the AI model."
