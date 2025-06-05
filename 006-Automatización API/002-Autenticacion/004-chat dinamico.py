import os
from openai import OpenAI

client = OpenAI(api_key="")
while True:
    pregunta = input("tu: ")
    response = client.responses.create(
        model="gpt-4o",
        input=pregunta
    )

    print("chatgpt: "+response.output_text)