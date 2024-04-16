from pyautocad import Autocad, APoint

# Initial setup
acad = Autocad(create_if_not_exists=True)
acad.prompt("Drawing trapezoidal hexagon...\n")

# Step 1: Drawing the top horizontal line of the trapezoid
start_point = APoint(0, 0)
end_point_horizontal_top = start_point + APoint(800, 0)
acad.model.AddLine(start_point, end_point_horizontal_top)

# Step 2: Drawing the first isosceles side of the trapezoid (approximating angle visually)
end_point_right_iso = end_point_horizontal_top + APoint(625, 1250)  # approximately 45 degrees
acad.model.AddLine(end_point_horizontal_top, end_point_right_iso)

# Step 3: Drawing the other isosceles side of the trapezoid, mirrored
end_point_left_iso = start_point + APoint(-625, 1250)  # approximating the mirrored angle
acad.model.AddLine(start_point, end_point_left_iso)

# Step 4: Connecting the endpoints of the isosceles sides
# Theoretical calculation with approximation for horizontal components
end_point_horizontal_bottom = end_point_left_iso + APoint(2050, 0)
acad.model.AddLine(end_point_left_iso, end_point_horizontal_bottom)

# Step 5: Drawing the vertical sides of the bottom rectangle
bottom_left_vertical = end_point_left_iso + APoint(0, -750)
bottom_right_vertical = end_point_horizontal_bottom + APoint(0, -750)
acad.model.AddLine(end_point_left_iso, bottom_left_vertical)
acad.model.AddLine(end_point_horizontal_bottom, bottom_right_vertical)

# Step 6: Connecting the endpoints of the vertical lines
acad.model.AddLine(bottom_left_vertical, bottom_right_vertical)