"""
Docstring
"""
from openai import OpenAI

class GPT():

    def __init__(self):

        self.client = OpenAI()

    # Testing method
    def run(self):
        completion = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
            ]
        )

        return completion.choices[0].message
    
    def models(self):
        return self.client.models.list()
    
    # --- Want to build out each api endpoint ---

    # Chat
    def chat(self):
        pass

    # TTS

    # STT

    # Vision

    # Image gen

    # Moderation

    # Assistants
    

if __name__ == "__main__":
    ai = GPT()
    print(ai.models())