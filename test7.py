from pyautocad import Autocad, APoint

acad = Autocad()

# Drawing the square pile cap by connecting lines
cap_points = [APoint(0, 0), APoint(2700, 0), APoint(2700, 2700), APoint(0, 2700), APoint(0, 0)]
for i in range(4):
    acad.model.AddLine(cap_points[i], cap_points[i+1])

# Calculating the center points of the circles (piles)
cap_center = APoint(1350, 1350)
offset = 625  # Half of the spacing
pile_centers = [cap_center + APoint(-offset, -offset), cap_center + APoint(offset, -offset),
                cap_center + APoint(offset, offset), cap_center + APoint(-offset, offset)]

# Drawing the circular piles
for center in pile_centers:
    acad.model.AddCircle(center, 250)  # Radius is half the diameter (500/2)

# Adding dimension for one side of the pile cap
dim_start = APoint(0, -100)  # Starting outside the square for visibility
dim_end = APoint(2700, -100)
text_pos = APoint(1350, -150)
acad.model.AddDimAligned(dim_start, dim_end, text_pos)

# Adding dimension for center-to-center spacing of circular piles
dim_center_start = pile_centers[0]  # Using first and second circles for horizontal dimension
dim_center_end = pile_centers[1]
text_pos_center = APoint((dim_center_start.x + dim_center_end.x)/2, dim_center_start.y - 100)
acad.model.AddDimAligned(dim_center_start, dim_center_end, text_pos_center)

