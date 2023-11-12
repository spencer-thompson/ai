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
            temp: float = 0.7,

    ):
        """Constructor"""
        self.sys_msg = [
            {"role": "system", "content": sys_msg}
        ]
        self.messages = messages
        self.model = model
        self.temp = temp

        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_KEY"),
        )

    def __str__(self):
        """String representation of the AI"""
        return f"Model: {self.model} | Temperature: {self.temp}"
    
    def models(self):
        """Returns all OpenAI models"""
        return self.client.models.list()
    
    def update_model(self, new_model: str) -> None:
        """Updates the model"""
        self.model = new_model
    
    # --- Want to build out each api endpoint ---

    # Chat
    def chat(self, query: str):
        """Chat conversation"""

        self.add_msg(role = "user", content = query)

        completion = self.client.chat.completions.create(
            model = self.model,
            messages = self.sys_msg + self.messages,
            temperature = self.temp,
        )

        self.add_msg(
            role = completion.choices[0].message.role,
            content = completion.choices[0].message.content
        )

        return completion.choices[0].message.content

    def chats(self, query: str):
        """Streaming Chat conversation"""

        self.add_msg(role = "user", content = query)

        completion = self.client.chat.completions.create(
            model = self.model,
            messages = self.sys_msg + self.messages,
            temperature = self.temp,
            stream = True
        )

        total_response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None: # Will change for function calling
                yield chunk.choices[0].delta.content
                total_response += chunk.choices[0].delta.content

        self.add_msg(role = "assistant", content = total_response)

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

    # --- Messages Control ---

    def add_msg(self, role: str, content: str):
        """Adds a new message to context"""
        self.messages.append({"role": role, "content": content})
    

if __name__ == "__main__":
    ai = GPT()
    print(ai.run())