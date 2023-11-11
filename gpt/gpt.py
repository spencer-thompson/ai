"""
Docstring
"""
import os

from openai import OpenAI
from dotenv import load_dotenv


class GPT():

    def __init__(
            self,
            sys_msg: str = "You are a helpful assistant.",
            messages: list = [],
            model: str = "gpt-4-1106-preview",

    ):

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
        """Returns all OpenAI models"""
        return self.client.models.list()
    
    # --- Want to build out each api endpoint ---

    # Chat
    def chat(self):
        """Chat conversation"""
        pass

    def chats(self):
        """Streaming Chat conversation"""
        pass

    def speech(self):
        """TTS"""
        pass

    def whisper(self):
        """STT"""
        pass

    # Image gen

    # Moderation
    def mod(self, message: str):
        """Moderation, pass in a string to get moderation scores."""
        return self.client.moderations.create(input=message)

    # Assistants
    

if __name__ == "__main__":
    ai = GPT()
    print(ai.run())