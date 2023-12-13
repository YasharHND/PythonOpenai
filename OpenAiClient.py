import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def list_models():
    return client.models.list()


def generate_ideas(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant designed to output JSON."
        }, {
            "role": "user",
            "content": prompt
        }]
    )
    content = json.loads(response.choices[0].message.content)
    _, (_, ideas) = next(enumerate(content.items()))
    return ideas


def generate_image(prompt, size):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality="hd",
        n=1
    )
    return response.data[0].url


def generate_image_title(image_url):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[{
            "role": "user",
            "content": [{
                "type": "text",
                "text": "Give me a cool simplified title for this image"
            }, {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                }
            }]
        }, {
            "role": "user",
            "content": "do NOT put the text in quotes"
        }]
    )
    return response.choices[0].message.content.strip("\"' ")


def suggest_image_tags(image_url, max_count):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[{
            "role": "user",
            "content": [{
                "type": "text",
                "text": f"Give me up to {max_count} tags that are most suitable for this image"
            }, {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                }
            }]
        }, {
            "role": "user",
            "content": "return a comma separated list"
        }]
    )
    return [tag.strip().lower() for tag in response.choices[0].message.content.split(",")]
