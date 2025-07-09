# nlp_engine.py

from langchain.chat_models import ChatOpenAI
import os
def ask_llm(prompt_text):
    try:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.2,
        )
        response = llm.invoke(prompt_text)
        return response.content
    except Exception as e:
        print(f"LLM error: {e}")
        return "Sorry, there was an error talking to the AI model."



    response = llm.predict(prompt_text)
    return response
