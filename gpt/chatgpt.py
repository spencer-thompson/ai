from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

messages = [
    {"role": "system", "content": "Explain api endpoints like the user is 5"}
]

user_input = input('User: ')
while user_input != 'q':

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model = "gpt-4-1106-preview",
        messages = messages,
        stream = True
    )

    total_response = ''
    print("Assistant: ", end='')
    for chunk in completion:
        print(chunk.choices[0].delta.content, end='')
        if chunk.choices[0].delta.content is not None:
            total_response += chunk.choices[0].delta.content

    messages.append({"role": "user", "content": total_response})

    print()
    print()
    user_input = input('User: ')
    print()