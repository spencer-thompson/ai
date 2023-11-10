"""
Docstring
"""
from openai import OpenAI

class GPT():

    def __init__(self):

        self.client = OpenAI()

    def run(self):
        completion = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
            ]
        )

        return completion.choices[0].message
    

if __name__ == "__main__":
    ai = GPT()
    print(ai.run())