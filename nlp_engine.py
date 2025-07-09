# nlp_engine.py

from langchain.chat_models import ChatOpenAI
import os

def ask_llm(prompt_text):
    # Load your API key
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    llm = ChatOpenAI(
        openai_api_key=api_key,
        model_name="gpt-3.5-turbo",
        temperature=0.2
    )

    response = llm.predict(prompt_text)
    return response
