# image_gen.py

from openai import OpenAI
import os

def generate_image(prompt):
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    client = OpenAI(api_key=api_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    return response.data[0].url
