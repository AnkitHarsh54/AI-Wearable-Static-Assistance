# nlp_engine.py

from huggingface_hub import InferenceClient
import streamlit as st

def ask_llm(prompt_text):
    if not prompt_text.strip():
        return "Please enter a question."

    try:
        hf_token = st.secrets["HF_TOKEN"]
        model_id = "google/flan-t5-base"

        client = InferenceClient(model=model_id, token=hf_token)

        result = client.text_generation(
            prompt_text,
            max_new_tokens=200,
            temperature=0.2,
        )
        return result

    except Exception as e:
        st.error(f"LLM error: {e}")
        return "Sorry, there was an error talking to the AI model."
