import base64
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.environ['OPENAI_API'])

def chat_completion(message):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": message}
    ],
    max_tokens=500
  )
  return response.choices[0].message.content
