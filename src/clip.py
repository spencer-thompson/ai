import pyperclip
import pyaudio
from pydub import AudioSegment
from plyer import notification

import io
import asyncio
from openai import AsyncOpenAI

from env import openai_key
from gpt import GPT


client = AsyncOpenAI(
    api_key=openai_key
)

p = pyaudio.PyAudio()

async def voice(content: str):
    # ai = GPT()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=2,
        rate=44100,
        output=True
    )

    response = await client.audio.speech.create(
        model="tts-1",
        voice="nova",
        response_format="mp3",
        # input=ai.chat("tell me a two sentence bedtime story"),
        input="Let me take a look and help you out",
        speed=1
    )
    # stream.start_stream()
    
    async for chunk in response.response.aiter_bytes(chunk_size=4096):
        stream.write(await decode_opus(chunk))
        # await asyncio.sleep(1)
    # stream.stop_stream()
    stream.close()
    p.terminate()

async def decode_opus(chunk):
    buffer = io.BytesIO(chunk)
    audio = AudioSegment.from_file(buffer, format='mp3')
    pcm = io.BytesIO()
    audio.export(pcm, format='wav')
    return pcm.getvalue()


# async def notify(content: str):
#     ai = GPT(sys_msg="You are a helpful assistant, you respond in Two Sentences or less.")
#     notification.notify(
#         title='GPT',
#         message=ai.chat(content),
#         app_name='Assistant',
#         app_icon='openai64.ico',
#         timeout=10,
#     )


async def main():
    
    clipboard = pyperclip.paste()
    await voice(clipboard) #, notify(clipboard)))
    # pyperclip.copy()


if __name__ == "__main__":
    asyncio.run(main())