from pyautocad import Autocad, APoint
import math

# Initialize AutoCAD application
acad = Autocad(create_if_not_exists=True)

# Define start and end points for lines
start_point_line1 = APoint(0, 0)
end_point_line1 = APoint(2050, 0)

start_point_line2 = APoint(0, 0)
end_point_line2 = APoint(0, 750)

start_point_line3 = APoint(2050, 0)
end_point_line3 = APoint(2050, 750)

# Calculate end points for Line 4 using given formula
alpha_line4 = math.radians(60)  # Convert degrees to radians
end_point_line4_x = 0 + 1250 * math.cos(alpha_line4)
end_point_line4_y = 750 + 1250 * math.sin(alpha_line4)
end_point_line4 = APoint(end_point_line4_x, end_point_line4_y)

# Calculate end points for Line 5 using given formula
alpha_line5 = math.radians(120)  # Convert degrees to radians
end_point_line5_x = 2050 + 1250 * math.cos(alpha_line5)
end_point_line5_y = 750 + 1250 * math.sin(alpha_line5)
end_point_line5 = APoint(end_point_line5_x, end_point_line5_y)

# Calculate start points for Line 4 and Line 5
start_point_line4 = APoint(0, 750)
start_point_line5 = APoint(2050, 750)

# Calculate start and end points for Line 6
start_point_line6 = end_point_line4
end_point_line6 = end_point_line5

# Draw lines
acad.model.AddLine(start_point_line1, end_point_line1)
acad.model.AddLine(start_point_line2, end_point_line2)
acad.model.AddLine(start_point_line3, end_point_line3)
acad.model.AddLine(start_point_line4, end_point_line4)
acad.model.AddLine(start_point_line5, end_point_line5)
acad.model.AddLine(start_point_line6, end_point_line6)