from pyautocad import Autocad, APoint
import math

# Initialize AutoCAD application
acad = Autocad()

# Define function to draw line given start point, length, and angle
def draw_line(start, length, angle):
    rad = math.radians(angle)
    end = APoint(start.x + length * math.cos(rad), start.y + length * math.sin(rad))
    acad.model.AddLine(start, end)
    return end

# Drawing the hexagon
start_point = APoint(0, 0)
length = 800
angles = [0, 60, 120, 180, 240, 300]

for angle in angles:
    end_point = draw_line(start_point, length, angle)
    start_point = end_point