from openai import OpenAI
import subprocess
import base64
import os


model = OpenAI()
model.timeout = 30

def image_b64(image):
    with open(image, "rb") as f:
        return base64.b64encode(f.read()).decode()


def visionExtract(b64_image, prompt):
    response = model.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "You a web scraper, your job is to extract information based on a screenshot of a website & user's instruction",
            }
        ] + [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{b64_image}",
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ]
            }
        ],
        max_tokens=1024,
    )

    message = response.choices[0].message
    message_text = message.content

    if "ANSWER_NOT_FOUND" in message_text:
        print("ERROR: Answer not found")
        return "I was unable to find the answer on that website. Please pick another one"
    else:
        print(f"GPT: {message_text}")
        return message_text



b64_image = image_b64("screenshot.jpg")
response = visionExtract(b64_image, "what is the weather of beijing today?")
print(response)