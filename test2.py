from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Drawing a square pile cap and piles inside it.\n")

# Draw square pile cap
pile_cap_pt1 = APoint(0, 0)
pile_cap_pt2 = APoint(2700, 2700)
acad.model.AddRectangle(pile_cap_pt1, pile_cap_pt2.x - pile_cap_pt1.x, pile_cap_pt2.y - pile_cap_pt1.y)

# Function to draw a circle (pile) given bottom left corner of square and offsets
def draw_pile(square_bottom_left, x_offset, y_offset, radius):
     center_pt = APoint(square_bottom_left.x + x_offset, square_bottom_left.y + y_offset)
     acad.model.AddCircle(center_pt, radius)

# Pile offsets and dimensions
x_offset, y_offset, radius = 1250, 1250, 500 / 2

# Draw piles
draw_pile(pile_cap_pt1, x_offset, y_offset, radius)
draw_pile(pile_cap_pt1, pile_cap_pt2.x - x_offset, y_offset, radius)
draw_pile(pile_cap_pt1, x_offset, pile_cap_pt2.y - y_offset, radius)
draw_pile(pile_cap_pt1, pile_cap_pt2.x - x_offset, pile_cap_pt2.y - y_offset, radius)

# Commands below require user interaction, not executable through PyAutoCAD
# Additional steps to add center-center dimensions & style them (Steps 4-6), are manual steps in AutoCAD environment