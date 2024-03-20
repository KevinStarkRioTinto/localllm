#!/usr/bin/python

# https://medium.com/@eboraks/llama-2-prompt-engineering-extracting-information-from-articles-examples-45158ff9bd23

from openai import OpenAI
import pandas
from datetime import datetime

df = pandas.read_excel(
    "data/rt-2023-simple.xlsx", 
    sheet_name='Rio Tinto Production Summary',
)
table = df.to_markdown(tablefmt="github", index=False)
print(table)

url = "http://localhost:8000/v1"

print(f"{url:*^50}")
client = OpenAI(
    api_key="foo",
                base_url=url,
)
sys = [
    {
        "role": "system",
        "content": f"""
            You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  
            If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. 
            If you don't know the answer to a question, please don't share false information.
            Today's date is {datetime.now().isoformat()}.
        """
    },
]
# chat_completion = client.chat.completions.create(
#     model="",
#     messages=sys + [
#         {
#             "role": "user",
#             "content": f"""
#                 Consider the following commodity production table. What reporting periods are available?
#                 ----
#                 table: 
#                 {table}
#             """
#         },
#     ]
# )
# for choice in chat_completion.choices:
#     print(choice.message.content)
    
# chat_completion = client.chat.completions.create(
#     model="",
#     messages=sys + [
#         {
#             "role": "user",
#             "content": f"""
#                 Consider the following commodity production table. What commodities are reported?
#                 ----
#                 table: 
#                 {table}
#             """
#         },
#     ]
# )
# for choice in chat_completion.choices:
#     print(choice.message.content)

    
chat_completion = client.chat.completions.create(
    model="",
    messages=sys + [
        {
            "role": "user",
            "content": f"""
                Consider the following commodity production table. 
                What is the 2023 Iron Ore production?
                ----
                {table}
            """
        },
    ]
)
for choice in chat_completion.choices:
    print(choice.message.content)

