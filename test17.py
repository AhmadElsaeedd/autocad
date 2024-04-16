from pyautocad import Autocad, APoint
import math

acad = Autocad()
acad.prompt("Script Starting...")
acad.doc.ActiveLayer = "0"

# Calculate the endpoint of the isosceles sides of the trapezoid
def calc_endpoint(x, y, angle_deg, length):
    angle_rad = math.radians(angle_deg)
    return APoint(x + length * math.cos(angle_rad), y + length * math.sin(angle_rad))

# 1. Draw the first side of the trapezoid
start_point = APoint(0, 0)
end_point1 = APoint(800, 0)
acad.model.AddLine(start_point, end_point1)

# 2. Draw the first isosceles side
end_point2 = calc_endpoint(end_point1.x, end_point1.y, 120, 1250)
acad.model.AddLine(end_point1, end_point2)

# 3. Draw the second isosceles side
end_point3 = calc_endpoint(start_point.x, start_point.y, 60, 1250)
acad.model.AddLine(start_point, end_point3)

# 4. First vertical side
end_point4 = APoint(end_point3.x, end_point3.y - 750)
acad.model.AddLine(end_point3, end_point4)

# 5. Second vertical side
end_point5 = APoint(end_point2.x, end_point2.y - 750)
acad.model.AddLine(end_point2, end_point5)

# 6. Bottom horizontal side to complete the figure
acad.model.AddLine(end_point4, end_point5)