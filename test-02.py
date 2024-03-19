#!/usr/bin/python

# https://medium.com/@eboraks/llama-2-prompt-engineering-extracting-information-from-articles-examples-45158ff9bd23

from openai import OpenAI

text = open('test-02-data.md').read()

url = "http://localhost:8000/v1"

print(f"{url:*^50}")
client = OpenAI(
    api_key="foo",
                base_url=url,
)
chat_completion = client.chat.completions.create(
    model="",
    messages=[
        {
            "role": "system",
            "content": """
                You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  
                Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. 
                Please ensure that your responses are socially unbiased and positive in nature.
                If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
                If you don't know the answer to a question, please don't share false information.
            """
        },
        {
            "role": "user",
            "content": f"""
                Write a concise TL;DR summary in numeric bullet-points for the following article, don't repeat ideas in bullet points.
                Limit the number of bullet-point to 5.
                ----
                article: 
                {text}
            """
        },
    ]
)
for choice in chat_completion.choices:
    print(choice.message.content)