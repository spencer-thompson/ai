"""
Docstring
"""
import os

from openai import OpenAI
from dotenv import load_dotenv

class GPT():

    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            organization=os.getenv('OPENAI_ORG_ID')
        )

    def run(self):
        completion = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
            ]
        )

        return completion.choices[0].message