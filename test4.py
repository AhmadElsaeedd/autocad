from pyautocad import Autocad, APoint

# Initialize AutoCAD
acad = Autocad(create_if_not_exists=True)
acad.prompt("Starting drawing...\n")
print(acad.doc.Name)

# Draw square pile cap
# First corner point of the square
p1 = APoint(0, 0)
# Second corner point calculated as @2700,2700 from the first point
p2 = p1 + APoint(2700, 2700)
square_pile_cap = acad.model.AddRectangle(p1, p2.x - p1.x, p2.y - p1.y)

# Draw first pile at one corner of the square
center_of_circle = p1  # Center of the circle at the corner of the square
radius = 250  # Half of the diameter
first_pile = acad.model.AddCircle(center_of_circle, radius)

# Copy first pile to create three more copies
base_point = center_of_circle
for displacement in [(2700, 0), (0, 2700), (-2700, 0)]:
    displacement_point = APoint(*displacement)
    copied_pile = acad.model.Copy(first_pile, base_point, base_point + displacement_point)

# Annotate dimensions for the square pile cap. Since PyAutoCAD does not 
# explicitly support adding dimensions directly via the library's API,
# we would typically resort to using AutoCAD's commands through 
# the Command() function, which is not detailed in the documentation excerpts provided.

# Similarly, setting properties such as line type to 'Dotted' for dimension lines
# would be managed through accessing the properties of the AutoCAD object
# and modifying them directly or via AutoCAD's command interface, not shown in provided documents.