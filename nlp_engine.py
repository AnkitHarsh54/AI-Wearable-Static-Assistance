from groq import Groq
import streamlit as st
import traceback

def ask_llm(prompt_text):
    if not prompt_text.strip():
        return "Please enter a question."

    try:
        api_key = st.secrets["GROQ_API_KEY"]

        client = Groq(api_key=api_key)

        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt_text
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        st.error(f"LLM error: {e}")
        st.code(traceback.format_exc())
        return "Sorry, there was an error talking to the AI model."
