import json

from authorized_client import client


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
