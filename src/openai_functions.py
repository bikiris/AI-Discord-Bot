import base64
import os
import urllib
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ['OPENAI_API'])


def chat_completion(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=message,
        max_tokens=400
    )
    print("In chat completion", response)
    return response.choices[0].message.content


def image_generation(message):
    response = client.images.generate(
        model="dall-e-2",
        prompt=message,
        size="256x256",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    urllib.request.urlretrieve(image_url, "AI.png")
    return image_url


# work in progress with command
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def stream_gpt_vision(query, image_path):
    base64_image = encode_image(image_path)
    image_input = [
        {
            "type": "text",
            "text": query,
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system",
             "content": "You are professional meme generator. Give me one meme caption for this image. Return only "
                        "the caption"},
            {"role": "user", "content": image_input}
        ],
        max_tokens=500
    )
    print(response.choices[0].message.content)
    return response
