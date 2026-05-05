import requests
from dotenv import load_dotenv
import os
import json 

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_URL = "https://api.openai.com/v1/responses"

HEADERS = {"Content-Type":"application/json", "Authorization": f"Bearer {OPENAI_API_KEY}"}

DATA = {"model": "gpt-5.5", "input": "what is the capital of USA?"}

response = requests.post(OPENAI_URL,headers=HEADERS,data=json.dumps(DATA))

print(response.json())