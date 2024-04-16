from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

# Step 1: Base horizontal line
start_point = APoint(0, 0)
end_point_base_line = APoint(2050, 0)
acad.model.AddLine(start_point, end_point_base_line)

# Step 2: First vertical side
end_point_first_vertical_side = APoint(2050, 750)
acad.model.AddLine(end_point_base_line, end_point_first_vertical_side)

# Step 3: Second vertical side
end_point_second_vertical_side = APoint(0, 750)
acad.model.AddLine(start_point, end_point_second_vertical_side)

# Since direct calculation of angle is not viable, defining points based on the description for angled connections:
# Assuming the hypothetical points for connections
# Hypothetical end point calculations for the 1250 mm line at an angle from (2050, 750) towards the center top
end_point_first_angled_line = APoint(1250, 1050)  # This is a placeholder
# Hypothetical end point calculations for the 1250 mm line at an angle from (0, 750) towards the center top
end_point_second_angled_line = APoint(800, 1050)  # This is a placeholder

# Step 4: First 1250 mm angled line - Placeholder
acad.model.AddLine(end_point_first_vertical_side, end_point_first_angled_line)

# Step 5: Second 1250 mm angled line - Placeholder
acad.model.AddLine(end_point_second_vertical_side, end_point_second_angled_line)

# Step 6: Top horizontal connecting line - Placeholder as the connection points are hypothetical
acad.model.AddLine(end_point_first_angled_line, end_point_second_angled_line)