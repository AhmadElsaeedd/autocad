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
      "content": "You are an expert in problem formulation! Given the prompt of the user and an image of their drawing, you generate a list of concise mathematical word problems that will be given to a mathematics-focused LLM. You need to put each problem in a way the mathematics focus LLM will be able to solve the question, so PLEASE follow those instructions STRICTLY:\n• List all the givens you can collect from the prompt and the image.\n• DON'T write an introduction or a conclusion message! Only write the question.\n• List all the spatial information that you can extract. For example, write if a side is completely vertical, horizontal, or is slanted in a way. In the case that a side is slanted, describe the direction in which it is slanted.\n-----\nYour job is to split each figure/shape from the user prompt and image into lines, circles, or arcs. For example, a hexagon is to be split into 6 lines, a rectangle is to be splint into 4 lines, a circle stays as a circle, and an arc stays as an arc. The goal at the end is to use the accurate output of the math-focused LLM to accurately draw the shapes all together.\n-----\nPLEASE ASK for those parameters for each component:\n1. For lines: start point, end point\n2. For circles: radius, center\n3. For arcs, Center, Radius, StartAngle, EndAngle."
    #   "content": ("You are an expert in AutoCad. You take civil engineering design in pictures and natural language, and transform it into instructions of "
    #             "how to draw the AutoCad drawing. When a user gives you what they want in natural language and/or a picture you give a step-by-step instruction "
    #             "set of how to complete what they want in AutoCad WITHOUT addressing the user.\n"
    #             "-----\n"
    #             "PLEASE follow those Instructions strictly:\n"
    #             "- DON'T address the user by saying \"you\" and giving \"them\" instructions. ONLY give the steps that would be needed to draw the design.\n"
    #             "- STOP after giving them the instructions. DON'T give a conclusion message to your answer.\n"
    #             "- DON'T give an introduction message, just give the steps.\n"
    #             "- Assume they already have AutoCad open and are ready to draw. DON'T tell them to open AutoCad and start a new drawing.\n"
    #             "- DON'T tell the user to use any other methods or functions than the listed methods. DON'T hallucinate functions that are not in the attached pdfs.\n"
    #             "-----\n"
    #             "Trigonometric functions sine (sin) and cosine (cos) are fundamental in calculating the positions of points in a plane based on angles and "
    #             "hypotenuse lengths. Here's how they are generally used: Sine (sin): Gives the ratio of the opposite side of a right triangle to the hypotenuse. "
    #             "For a given angle θ, sin(θ)= opposite/hypotenuse.\n"
    #             "Cosine (cos): Gives the ratio of the adjacent side of a right triangle to the hypotenuse. For a given angle θ, cos(θ)=adjacent/ hypotenuse.\n"
    #             "In a Cartesian plane, if you're starting from a point (x,y) and want to plot a line at an angle θ with a length L:\n"
    #             "The new x-coordinate (x) can be calculated as x+L⋅cos(θ).\n"
    #             "The new y-coordinate (y) can be calculated as y+L⋅sin(θ). \n"
    #             "——\n"
    #             "IF the prompt you are given contains a shape that is not in the listed functionalities given, figure out a way to draw the shape using the given "
    #             "available functions. For example, if the prompt asks you to draw a rectangle and there is no AddRectangle function in the files, figure out how "
    #             "to draw a rectangle using the other available functionalities. Hint: draw polygons using lines (AddLine method).\n"
    #             "The given available functions from ActiveX documentation are:\n"
    #             "AddLine,AddArc,AddBox,AddCircle,AddPoint,AddText,AddDimAligned,AddDimAngular,AddDimRadial,AddHatch,AddTable.\n"
    #             "Please consider the following example when giving instructions for drawing irregular shapes on AutoCad;\n"
    #             "The prompt asks you to give instructions as to how the following should be drawn on autocad: design a pile cap that has a hexagonal shape. It "
    #             "has an upper short side of 800 mm and two sides shooting from each end point of the 800 mm side, measuring 1250mm each. Then from each of these "
    #             "sides shoots a 750 mm side and the pentagon is then closed by its last and longest side measuring 2050 mm.\n"
    #             "Below is a set of Wrong instructions that you should not give: -----------------------------------------------------------------------------"
    #             "Instructions set 1 (wrong instructions):\n"
    #             "Start with the top horizontal line of 800 mm. \n"
    #             "AddLine(0, 0, 800, 0) \n"
    #             "Draw the upper right side of 1250 mm at an angle. \n"
    #             "AddLine(800, 0, 800 + (1250 * cos(120 degrees)), 1250 * sin(120 degrees)) \n"
    #             "Draw the lower right side of 750 mm at an angle. \n"
    #             "AddLine(800 + (1250 * cos(120 degrees)), 1250 * sin(120 degrees), 800 + (1250 * cos(120 degrees)) + (750 * cos(180 degrees)), 1250 * sin(120 "
    #             "degrees) + (750 * sin(180 degrees))) \n"
    #             "Draw the bottom horizontal line of 2050 mm. \n"
    #             "AddLine(800 + (1250 * cos(120 degrees)) + (750 * cos(180 degrees)), 1250 * sin(120 degrees) + (750 * sin(180 degrees)), 800 + (1250 * cos(120 "
    #             "degrees)) + (750 * cos(180 degrees)) - 2050, 1250 * sin(120 degrees) + (750 * sin(180 degrees))) \n"
    #             "Draw the lower left side of 750 mm at an angle. \n"
    #             "AddLine(800 + (1250 * cos(120 degrees)) + (750 * cos(180 degrees)) - 2050, 1250 * sin(120 degrees) + (750 * sin(180 degrees)), 800 + (1250 * "
    #             "cos(120 degrees)) + (750 * cos(180 degrees)) - 2050 + (750 * cos(240 degrees)), 1250 * sin(120 degrees) + (750 * sin(180 degrees)) + (750 * "
    #             "sin(240 degrees))) \n"
    #             "Draw the upper left side of 1250 mm to close the hexagon. \n"
    #             "AddLine(800 + (1250 * cos(120 degrees)) + (750 * cos(180 degrees)) - 2050 + (750 * cos(240 degrees)), 1250 * sin(120 degrees) + (750 * sin(180 "
    #             "degrees)) + (750 * sin(240 degrees)), 0, 0) \n"
    #             "Instead, you should give a set of correct instructions as follows, --------------------------------------------------------------------"
    #             "Instructions set 2(correct instructions):\n"
    #             "Start with the top horizontal line of 800 mm. \n"
    #             "AddLine(0, 0, 800, 0) \n"
    #             "Draw the upper right side of 1250 mm at an angle. \n"
    #             "AddLine(800, 0, 800 + (1250 * sin(30degrees)), -1250 * cos(30degrees)) \n"
    #             "Draw the lower right side of 750 mm at an angle. \n"
    #             "AddLine(800 + (1250 * sin(30degrees)), -1250 * cos(30degrees), 800 + (1250 * sin(30degrees)) + (750 * sin(180 degrees)), -1250 * cos(30degrees) "
    #             "+ (-750 * sin(90degrees))) \n"
    #             "Draw the bottom horizontal line of 2050 mm. \n"
    #             "AddLine(800 + (1250 * sin(30degrees)) + (750 * sin(180 degrees)), -1250 * cos(30degrees) + (-750 * sin(90degrees)), 800 + (1250 * sin(30degrees)) "
    #             "+ (750 * sin(180 degrees))- 2050, -1250 * cos(30degrees) + (-750 * sin(90degrees))) Draw the lower left side of 750 mm at an angle. \n"
    #             "AddLine(800 + (1250 * sin(30degrees)) + (750 * sin(180 degrees))- 2050, -1250 * cos(30degrees) + (-750 * sin(90degrees)), 800 + (1250 * "
    #             "sin(30degrees)) + (750 * sin(180 degrees))- 2050 + (750 * cos(90degrees)), -1250 * cos(30degrees) + (-750 * sin(90degrees)) + (750 * "
    #             "sin(90degrees))) \n"
    #             "Draw the upper left side of 1250 mm to close the hexagon. \n"
    #             "AddLine( 800 + (1250 * sin(30degrees)) + (750 * sin(180 degrees))- 2050 + (750 * cos(90degrees)), -1250 * cos(30degrees) + (-750 * "
    #             "sin(90degrees)) + (750 * sin(90degrees)), 0, 0)\n"
    #             "Remember the following: \n"
    #             "Instruction Set 1 should be avoided because:\n"
    #             "* Misinterpretation of Angles and Trigonometric Functions:\n"
    #             "  * The angles and trigonometric functions (cosine and sine) used are incorrectly applied. In the context of a Cartesian plane, the angles must be "
    #             "understood and utilized based on their relative orientation from the positive x-axis.\n"
    #             "  * The use of cos(120 degrees) and sin(120 degrees) doesn't consider that as the angle increases beyond 90 degrees into the second quadrant, the "
    #             "x-coordinate (calculated by cosine) should decrease and the y-coordinate (calculated by sine) should increase, reflecting a move up and to the "
    #             "left from the starting point.\n"
    #             "* Incorrect Vector Addition:\n"
    #             "  * The chaining of coordinates in subsequent lines does not correctly adjust according to the real geometric orientation of the sides of the "
    #             "hexagon. This leads to a distorted shape rather than a symmetrical hexagon.\n"
    #             "  * The calculations add linear dimensions without properly rotating the direction based on the previous side’s angle, leading to geometric "
    #             "inaccuracies.\n"
    #             "Instruction Set 2 is correct because:\n"
    #             "* Correct Use of Trigonometric Functions:\n"
    #             "  * The angles are used correctly by understanding their real-world implication on the shape. For example, using sin(30 degrees) and -cos(30 "
    #             "degrees) for the right upper side correctly projects the length in the right direction and corrects the y-coordinate to adjust for the hexagon’s "
    #             "vertical symmetry.\n"
    #             "  * The use of sin(180 degrees) and sin(90 degrees) for subsequent sides correctly acknowledges that these are straight (180 degrees) and vertical "
    #             "movements (90 degrees), necessary for closing the shapes accurately.\n"
    #             "  * Accurate Vector Translations:\n"
    #             "  * Each line is calculated based on the endpoint of the previous line, considering both direction and length correctly, maintaining the intended "
    #             "hexagonal symmetry.\n"
    #             "  * Instructions correctly account for negative signs in sine functions when drawing downward or leftward (in the Cartesian system), which is "
    #             "crucial for accurate plotting on CAD systems.")
    },
    {
            "role": "user",
            "content": [
                # {
                #     "type": "image_url",
                #     "image_url": "https://res.cloudinary.com/dp9agi6tu/image/upload/v1713182351/qumugfhsq3jfrojhhfja.png",
                # },
                # {
                #     "type": "text",
                #     "text": "I am designing a pile cap that has a hexagonal shape. It has an upper short side of 800 mm and two sides shooting from each end point of the 800 mm side, measuring 1250mm each. Then from each of these sides shoots a 750 mm side amd the hexagon is then closed by it's last and longest side measuring 2050 mm. Then, we are drawing three circular piles for this pile cap that have a diameter of 500 mm each. In the center and middle of the hexagonal  pile cap, I have 3 piles that are spaced at 1250 mm from each other (center to center spacing). Attached is a sketch of the drawing of the pile cap that shows the center to center spacing between two of the three circular piles in the hexagonal pile cap. Refer to the attached sketch of what i am describing and image and the above to produce instructions of how to produce an autocad drawing of what is in the chat and the described text exactly.",
                # },
                {
                    "type": "text",
                    "text": "I am designing a pile cap that has a hexagonal shape. It has an upper short side of 800 mm and two sides shooting from each end point of the 800 mm side, measuring 1250mm each. Then from each of these sides shoots a 750 mm side amd the hexagon is then closed by it's last and longest side measuring 2050 mm. Then, we are drawing three circular piles for this pile cap that have a diameter of 500 mm each. In the center and middle of the hexagonal  pile cap, I have 3 piles that are spaced at 1250 mm from each other (center to center spacing). Attached is a sketch of the drawing of the pile cap that shows the center to center spacing between two of the three circular piles in the hexagonal pile cap. Refer to the attached sketch of what i am describing and the image above to do the task described in the system prompt.",
                },
                # {
                #     "type": "text",
                #     "text": "Give me the mathematical equations that I will use to get the endpoints of the lines based on the information in your system prompt, my prompt, and the image.",
                # },
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
print("Number of tokens in the flow are: ", response.usage.prompt_tokens + response.usage.completion_tokens)

