from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

messages = [
    {"role": "system", "content": "You are a chicken, you only respond with chicken noises"}
]

user_input = input('User: ')
while user_input != 'q':

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model = "gpt-4-1106-preview",
        messages = messages
    )

    messages.append(completion.choices[0].message)

    print()
    print(f'Assistant: {completion.choices[0].message.content}')
    print()
    user_input = input('User: ')