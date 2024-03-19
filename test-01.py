#!/usr/bin/python
from openai import OpenAI
from openai.types import CreateEmbeddingResponse, Embedding

url = "http://localhost:8000/v1"

print(f"{url:*^50}")
client = OpenAI(api_key="foo", base_url=url)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Always replace any feline reference or name with a canine equivalent.",
        },
        {
            "role": "user",
            "content": "Please write a haiku about purple cats",
        },
    ],
    model="",
)
for choice in chat_completion.choices:
    print(choice.message.content)