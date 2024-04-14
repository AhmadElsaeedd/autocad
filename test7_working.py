from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
#ToDo: a way to automate opening a new document for each code run (have to fork library and edit it myself)

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

# PROMPT:
# I am designing a square pile that has 4 piles in it. the dimensions for the pile cap are 2700 by 2700 mm. I am using circular piles of diameter 500 mm that are to be spaced at 1250 mm from each other (center to center spacing). After that all 4 piles should be grouped and centered in the middle of the square pile cap. I need a 2D sketch showing a cross-section of the pile cap with the pile placement in it. I want the dimensions of one side of the square pile cap to be shown as 2700 mm and i want the dimension of center to center horizontal spacing between the piles for two of the piles to be showing as 1250 mm

# INSTRUCTIONS:
# Start by creating a square pile cap. Use the AddLine method to draw four lines, each representing a side of the square pile cap with dimensions of 2700 mm by 2700 mm. Make sure to calculate the start and end points correctly so that the lines connect to form a perfect square.

# Use the AddCircle method to create four circular piles with a diameter of 500 mm. The center points of these circles should be calculated based on the desired spacing of 1250 mm between the centers of the piles. Since the pile cap is square and measures 2700 mm on each side, the center points need to be meticulously calculated to ensure that the piles are centered and properly spaced within the cap.

# The coordinates for the center of each pile can be calculated considering the square's center is at (1350, 1350) with respect to the pile cap's lower left corner.
# Subtracting and adding half of the spacing (625 mm) from the center point’s coordinates in both x and y directions will give the centers of the four piles.
# Use the AddDimAligned method to add dimensions showing one side of the square pile cap as 2700 mm. For this, set the exterior points of one side of the pile cap as the ExtLine1Point and ExtLine2Point, with the TextPosition appropriately located for clear visibility.

# Use the AddDimAligned method again to add dimensions showing the center-to-center horizontal spacing between two of the piles as 1250 mm. The ExtLine1Point and ExtLine2Point should be the center points of two adjacent piles, with the TextPosition placed in a clear spot to avoid confusion.