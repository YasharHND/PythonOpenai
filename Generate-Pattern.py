import webbrowser
from datetime import datetime

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="fabric pattern red roses and creamy background",
    size="1792x1024",
    quality="hd",
    n=1
)

image_url = response.data[0].url
print(image_url)
webbrowser.open(image_url)
print(datetime.now())
