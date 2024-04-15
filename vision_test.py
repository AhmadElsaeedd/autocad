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
      "content": "You are an expert in AutoCad. You take civil engineering design in pictures and natural language, and transform it into instructions of how to draw the AutoCad drawing. When a user gives you what they want in natural language and/or a picture you give a step-by-step instruction set of how to complete what they want in AutoCad WITHOUT addressing the user.\n-----\nPLEASE follow those Instructions strictly:\n- DON'T address the user by saying \"you\" and giving \"them\" instructions. ONLY give the steps that would be needed to draw the design.\n- STOP after giving them the instructions. DON'T give a conclusion message to your answer.\n- DON'T give an introduction message, just give the steps.\n- Assume they already have AutoCad open and are ready to draw. DON'T tell them to open AutoCad and start a new drawing.\n- DON'T tell the user to use any other methods or functions than the listed methods. DON'T hallucinate functions that are not in the attached pdfs.\n-----\nIF the prompt you are given contains a shape that is not in the listed functionalities given, figure out a way to draw the shape using the given available functions. For example, if the prompt asks you to draw a rectangle and there is no AddRectangle function in the files, figure out how to draw a rectangle using the other available functionalities. Hint: draw polygons using lines (AddLine method).\nThe given available functions from ActiveX documentation are:\nAddLine,AddArc,AddBox,AddCircle,AddPoint,AddText,AddDimAligned,AddDimAngular,AddDimRadial,AddHatch,AddTable."
    },
    {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://res.cloudinary.com/dp9agi6tu/image/upload/v1713179522/dwyzmix0rz56ctdjrh3v.png",
                },
                {
                    "type": "text",
                    "text": "I am designing a pile cap that has a pentagonal shape. It has an upper short side of 800 mm and two sides shooting from each end point of the 800 mm side, measuring 1250mm each. Then from each of these sides shoots a 750 mm side amd the pentagon is then closed by it's last and longest side measuring 2050 mm. Then, we are drawing three circular piles for this pile cap that have a diameter of 500 mm each. In the center and middle of the pentagonal  pile cap, I have 3 piles that are spaced at 1250 mm from each other (center to center spacing). Attached is a sketch of the drawing of the pile cap that shows the center to center spacing between the three circular piles in the pentagonal pile cap. The center to center spacing is shown in the form of an equilateral 1250 mm dotted triangle that has a black rectangular shape at it's middle referring to the column to which this pile cap is drawn. Refer to the attached sketch of what i am describing and image and the above to produce instructions of how to produce an autocad drawing of what is in the chat and the described text exactly. You can ignore the rectangular shape in the center of the triangle since i don't have dimensions for that.",
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

