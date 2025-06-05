import os
from openai import OpenAI

client = OpenAI(api_key="")

response = client.responses.create(
    model="gpt-4.1",
    input="Escribe una receta de cocina sana para comer hoy, pero no puedo cocinar, algo directamente de supermercado."
)

print(response.output_text)