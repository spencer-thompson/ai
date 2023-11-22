import pyperclip
import pyaudio
from pydub import AudioSegment
from plyer import notification
import opuslib
import numpy as np

import sounddevice as sd
import io

import io
import asyncio
from openai import OpenAI

from env import openai_key
from gpt import GPT


client = OpenAI(
    api_key=openai_key
)

p = pyaudio.PyAudio()


def stream_audio(sample_rate, frame_size):

    decoder = opuslib.Decoder(48000, 2)
    fps = 1000//frame_size
    spf = sample_rate//fps

    completion = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        response_format="opus",
        # input=ai.chat("tell me a two sentence bedtime story"),
        input="Let me take a look and help you out",
        speed=1
    )
    total = b''
    for chunk in completion.iter_bytes(chunk_size=4096):

        if chunk:

            # total += chunk
            # while len(chunk) >= frame_size:
            try:

                pcm_data = decoder.decode(chunk, spf)

                sd.play(pcm_data, samplerate=sample_rate)
                sd.wait()
                #buffer = buffer[frame_size:]
                total = b''
            except Exception as e:
                print(f"Error Processing chunk: {e}")
                break

def main():
    
    clipboard = pyperclip.paste()
    # voice(clipboard) #, notify(clipboard)))
    # pyperclip.copy()
    stream_audio(5)


if __name__ == "__main__":
    main()