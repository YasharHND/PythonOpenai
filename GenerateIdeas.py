import json

from openai import OpenAI


def generate_ideas(prompt):
    response = OpenAI().chat.completions.create(
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
