from pyautocad import Autocad, APoint

# Initialize AutoCAD application instance
acad = Autocad()
print(acad.doc.Name)

# Draw four circular piles
centers = [APoint(-625, 625), APoint(625, 625), APoint(-625, -625), APoint(625, -625)]
for center in centers:
    # x, y = center  # Explicitly unpack tuple to avoid any confusion
    # print(f"Adding circle at ({x}, {y}) with radius 250")
    acad.model.AddCircle(center, 250)

# Draw square pile cap
# vertices = [APoint(-1350, 1350), APoint(1350, 1350), APoint(1350, -1350), APoint(-1350, -1350), APoint(-1350, 1350)]
# acad.model.AddPolyline(vertices)
    # Draw Pile Cap using AddLine for each side
pile_cap_lines = [
    acad.model.AddLine(top_left, APoint(top_left.x + 2700, top_left.y)),  # Top side
    acad.model.AddLine(APoint(top_left.x + 2700, top_left.y), APoint(top_left.x + 2700, top_left.y - 2700)),  # Right side
    acad.model.AddLine(APoint(top_left.x + 2700, top_left.y - 2700), APoint(top_left.x, top_left.y - 2700)),  # Bottom side
    acad.model.AddLine(APoint(top_left.x, top_left.y - 2700), top_left)  # Left side
]

# Add dimension for one side of the square pile cap
acad.model.AddDimAligned((-1350, 1350), (1350, 1350), (0, 1500))

# Add dimension showing center to center spacing between two piles
acad.model.AddDimAligned((-625, 625), (625, 625), (0, 750))