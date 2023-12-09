from openai import OpenAI


def generate_title(prompt):
    response = OpenAI().chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "You are a helpful assistant."
        }, {
            "role": "user",
            "content": prompt
        }, {
            "role": "user",
            "content": "ignore the image generation hints like style, background type or padding settings, etc. in the title"
        }]
    )
    return response.choices[0].message.content
