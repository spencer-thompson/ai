"""
Docstring
"""
import os

from openai import OpenAI
from dotenv import load_dotenv

class GPT():

    def __init__(self):
        
        load_dotenv()
        client = OpenAI(
            organization=os.getenv('OPENAI_ORG_ID')
        )