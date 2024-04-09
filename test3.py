from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

# Pile Cap Dimensions
pile_cap_length = 2700

# Draw Pile Cap using Lines equivalent to RECTANG
def draw_square_pile_cap(bottom_left_corner, length):
    p1 = bottom_left_corner
    p2 = APoint(p1.x + length, p1.y)
    p3 = APoint(p2.x, p2.y + length)
    p4 = APoint(p1.x, p1.y + length)
    
    acad.model.AddLine(p1, p2)
    acad.model.AddLine(p2, p3)
    acad.model.AddLine(p3, p4)
    acad.model.AddLine(p4, p1)

# Define piles
def draw_pile(center, radius):
    acad.model.AddCircle(center, radius)

# Pile Cap Lower Left Corner
pile_cap_corner = APoint(0, 0)

# Draw Square Pile Cap
draw_square_pile_cap(pile_cap_corner, pile_cap_length)

# Define Piles Positions based on the Requested Offsets
piles_offsets = [(1250, 1250), (1450, 1250), (1250, 1450), (1450, 1450)]

# Draw Piles within Pile Cap
for offset in piles_offsets:
    draw_pile(APoint(pile_cap_corner.x + offset[0], pile_cap_corner.y + offset[1]), 250)  # Radius = 500 / 2