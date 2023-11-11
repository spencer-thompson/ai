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
            api_key=os.getenv("OPENAI_KEY"),
        )

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

    def chats(self):
        pass

    # TTS
    def speech(self):
        pass

    # STT
    def whisper(self):
        pass

    # Image gen

    # Moderation
    def mod(self, message: str):
        return self.client.moderations.create(input=message)

    # Assistants
    

if __name__ == "__main__":
    ai = GPT()
    print(ai.run())