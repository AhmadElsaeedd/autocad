from pyautocad import Autocad, APoint

acad = Autocad()

# Outer triangle
p1 = APoint(0, 0)
p2 = APoint(1025, 1750)
p3 = APoint(2050, 0)
acad.model.AddLine(p1, p2)
acad.model.AddLine(p2, p3)
acad.model.AddLine(p3, p1)

# Inner triangle calculations
inner_p1 = p1 + APoint(205, 350)
inner_p2 = p2 + APoint(0, -350)
inner_p3 = p3 - APoint(205, 350)

# Inner triangle creation
acad.model.AddLine(inner_p1, inner_p2)
acad.model.AddLine(inner_p2, inner_p3)
acad.model.AddLine(inner_p3, inner_p1)

# Center rectangle calculations
rect_p1 = (p1 + p2) / 2 - APoint(250, -875)
rect_p2 = rect_p1 + APoint(500, 0)
rect_p3 = rect_p2 + APoint(0, -1250)
rect_p4 = rect_p1 + APoint(0, -1250)

# Center rectangle creation
acad.model.AddLine(rect_p1, rect_p2)
acad.model.AddLine(rect_p2, rect_p3)
acad.model.AddLine(rect_p3, rect_p4)
acad.model.AddLine(rect_p4, rect_p1)

# Pile circles
center_left = rect_p1 + (rect_p3 - rect_p1) / 2 - APoint(375, 0)
center_right = rect_p1 + (rect_p3 - rect_p1) / 2 + APoint(375, 0)
acad.model.AddCircle(center_left, 250)
acad.model.AddCircle(center_right, 250)

# Dimensions and Annotations are not provided in the instructions, hence a generic approach
# This section should be where you add dimensions and text annotations.
# However, no specific guiding dimensions or text content were provided for this task.