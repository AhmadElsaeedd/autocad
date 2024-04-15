import base64
from openai import OpenAI

# Function to encode the image file to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Assuming you have an image named 'example.jpg' in the same directory
image_path = 'example.png'
base64_image = encode_image_to_base64(image_path)

client = OpenAI(api_key="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")

response = client.chat.completions.create(
  model="gpt-4-1106-vision-preview",
  messages=[
    {
      "role": "system",
      "content": "You are an expert in AutoCad. You take civil engineering design in pictures and natural language, and transform it into instructions of how to draw the AutoCad drawing. When a user gives you what they want in natural language or a picture you give a step-by-step instruction set of how to complete what they want in AutoCad WITHOUT addressing the user.\n-----\nPLEASE follow those Instructions strictly:\n- DON'T address the user by saying \"you\" and giving \"them\" instructions. ONLY give the steps that would be needed to draw the design.\n- STOP after giving them the instructions. DON'T give a conclusion message to your answer.\n- DON'T give an introduction message, just give the steps.\n- Assume they already have AutoCad open and are ready to draw. DON'T tell them to open AutoCad and start a new drawing.\n- DON'T tell the user to use any other methods or functions than the listed methods in your knowledge. DON'T hallucinate functions that are not in the attached pdfs.\n-----\nIF the prompt you are given contains a shape that is not in the files given, figure out a way to draw the shape using the given available functions. For example, if the prompt asks you to draw a rectangle and there is no AddRectangle function in the files, figure out how to draw a rectangle using the other available functionalities. Hint: draw polygons using lines (AddLine method)."
    },
    {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/42965434/original/68c484dceb646f96647b0e9258401c79c7513609/do-civil-and-mechanical-drawings.jpg",
                },
            ],
        }
  ],
  temperature=0.5,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)

