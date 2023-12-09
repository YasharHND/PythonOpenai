from openai import OpenAI


def generate_image(prompt, size="1792x1024"):
    response = OpenAI().images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality="hd",
        n=1
    )
    return response.data[0].url
