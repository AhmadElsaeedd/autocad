from pyautocad import Autocad, APoint

# Initialize AutoCAD application
acad = Autocad(create_if_not_exists=True)

# Pile cap corner offset calculation
pile_cap_offset = 2700 / 2

# Top-left corner of the pile cap (centered at the origin)
top_left = APoint(-pile_cap_offset, pile_cap_offset)

# Draw Pile Cap using AddLine for each side
pile_cap_lines = [
    acad.model.AddLine(top_left, APoint(top_left.x + 2700, top_left.y)),  # Top side
    acad.model.AddLine(APoint(top_left.x + 2700, top_left.y), APoint(top_left.x + 2700, top_left.y - 2700)),  # Right side
    acad.model.AddLine(APoint(top_left.x + 2700, top_left.y - 2700), APoint(top_left.x, top_left.y - 2700)),  # Bottom side
    acad.model.AddLine(APoint(top_left.x, top_left.y - 2700), top_left)  # Left side
]

# Calculate offsets from the center of the pile cap to the center of a pile
pile_center_offset = (2700 / 2) - (1250 / 2)

# Coordinates for the centers of the four piles
pile_centers = [
    APoint(-pile_center_offset, pile_center_offset),
    APoint(pile_center_offset, pile_center_offset),
    APoint(pile_center_offset, -pile_center_offset),
    APoint(-pile_center_offset, -pile_center_offset)
]

# Draw piles at calculated positions
piles = [acad.model.AddCircle(center, 250) for center in pile_centers]

# Add dimensions to each side of the pile cap
pile_cap_dimensions = [
    acad.model.AddDimAligned(top_left, APoint(top_left.x + 2700, top_left.y), APoint(top_left.x + 1350, top_left.y + 100)),
    acad.model.AddDimAligned(APoint(top_left.x + 2700, top_left.y), APoint(top_left.x + 2700, top_left.y - 2700), APoint(top_left.x + 2800, top_left.y - 1350)),
    acad.model.AddDimAligned(APoint(top_left.x + 2700, top_left.y - 2700), APoint(top_left.x, top_left.y - 2700), APoint(top_left.x + 1350, top_left.y - 2800)),
    acad.model.AddDimAligned(APoint(top_left.x, top_left.y - 2700), top_left, APoint(top_left.x - 100, top_left.y - 1350))
]

# Add dimension to show the center to center spacing between two opposite piles
dotted_line = acad.model.AddLine(pile_centers[0], pile_centers[2])
# dotted_line.Linetype = "Dotted"
spacing_dimension = acad.model.AddDimAligned(pile_centers[0], pile_centers[2], APoint(0, -900))