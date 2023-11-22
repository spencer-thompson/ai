import pyperclip
import pyaudio
from pydub import AudioSegment
from pyogg.opus import OpusDecoder
from plyer import notification
import opuslib
import numpy as np

import pyogg
import sounddevice as sd
import io
import threading

import io
import asyncio
from openai import OpenAI

from env import openai_key
from gpt import GPT


client = OpenAI(
    api_key=openai_key
)

p = pyaudio.PyAudio()

def voice(content: str):
    # ai = GPT()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=2,
        rate=48000,
        output=True
    )
    # stream = pyogg.OpusFileStream

    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        response_format="mp3",
        # input=ai.chat("tell me a two sentence bedtime story"),
        input="Let me take a look and help you out",
        speed=1
    )
    # stream.start_stream()
    
    for chunk in response.response.iter_bytes(chunk_size=4096):
        stream.write(decode_opus(chunk))
        # await asyncio.sleep(1)
    # stream.stop_stream()
    stream.close()
    p.terminate()

def decode_opus(chunk):
    decoder = OpusDecoder()
    #decoder.set_application("audio")
    decoder.set_channels(2)
    decoder.set_sampling_frequency(48000)
    return decoder.decode(chunk)


def stream_audio(sample_rate, frame_size):
    # Set up a streaming request to the server
    decoder = opuslib.Decoder(48000, 1)
    #buffer = bytearray()

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
        print(chunk)
    #response.iter_bytes(chunk_size=4096):
        # pcm_data = decoder.decode(chunk, frame_size)
        # pcm_data = np.frombuffer(chunk, dtype=np.int16).astype(np.float32) / 32768.0
        # sd.play(pcm_data, samplerate=48000)
        # sd.wait()
        
        if type(chunk) is bytes:
            #pcm_data = decoder.decode(chunk, frame_size)
            #sd.play(pcm_data, samplerate=48000)
            # sd.play(chunk.decode(encoding="opus"), samplerate=48000)
            # sd.wait()
            #buffer.extend(chunk)
            total += chunk
            while len(chunk) >= frame_size:
                try:
                    # Decode the Opus chunk to PCM
                    # Note: You need to adjust this part according to the actual Opus decoding method
                    #print(type(buffer))
                    # pcm_data = decoder.decode_float(bytes(buffer[:frame_size]), frame_size)
                    pcm_data = decoder.decode(total, frame_size)
                    #pcm_data = np.frombuffer(pcm_data, dtype=np.int16).astype(np.float32) / 32768.0

                    # Play the PCM data
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