from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv('OPENAI_KEY')
print("API KEY: ", api_key)
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4-1106-vision-preview",
  messages=[
    {
      "role": "system",
      "content": "If the user was to do math to draw the image on AutoCad what's in their image and their prompt, what would be the math needed and the knowns needed. You help in generating a prompt to input to the wolfram API so we can get the exact math needed. Generate the prompts in a comma-separated style even if they're full sentences. \nONLY give the prompts even if the user asks to generate a drawing or instructions."
    },
    {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://res.cloudinary.com/dp9agi6tu/image/upload/v1713182351/qumugfhsq3jfrojhhfja.png",
                },
                {
                    "type": "text",
                    "text": "I am designing a pile cap that has a hexagonal shape. It has an upper short side of 800 mm and two sides shooting from each end point of the 800 mm side, measuring 1250mm each. Then from each of these sides shoots a 750 mm side amd the hexagon is then closed by it's last and longest side measuring 2050 mm. Then, we are drawing three circular piles for this pile cap that have a diameter of 500 mm each. In the center and middle of the hexagonal  pile cap, I have 3 piles that are spaced at 1250 mm from each other (center to center spacing). Attached is a sketch of the drawing of the pile cap that shows the center to center spacing between two of the three circular piles in the hexagonal pile cap. Refer to the attached sketch of what i am describing and image and the above to produce instructions of how to produce an autocad drawing of what is in the chat and the described text exactly.",
                },
            ],
        }
  ],
  temperature=0.25,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)
