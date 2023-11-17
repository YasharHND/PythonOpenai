from dotenv import load_dotenv
from openai import OpenAI
import webbrowser

load_dotenv()

client = OpenAI()

response = client.images.generate(
    model="dall-e-2",
    prompt="fabric pattern green roses and creamy background",
    quality="hd",
    n=1
)

image_url = response.data[0].url
print(image_url)
webbrowser.open(image_url)
