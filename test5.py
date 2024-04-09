from pyautocad import Autocad, APoint

# Initialize AutoCad Automation
acad = Autocad()

# Drawing a square pile cap using AddLightWeightPolyline
points = [0, 0, 2700, 0, 2700, 2700, 0, 2700, 0, 0]  # Closing the square by defining a flat list of coordinates
pile_cap = acad.model.AddLightWeightPolyline(points)
pile_cap.Closed = True  # Ensuring the polyline is closed to form a square

# Drawing the first pile (Circle), center is at (0, 0) since that's the first vertex of the square
center_pile1 = APoint(0, 0)  # Creating an APoint for the center ensures compatibility with AddCircle
radius_pile = 250
pile1 = acad.model.AddCircle(center_pile1, radius_pile)

# Copying the first pile to create three more copies
# Center points for piles need explicit calculation based on the square's size
pile2_center = APoint(2700, 0)
pile3_center = APoint(0, 2700)
pile4_center = APoint(2700, 2700)

# Copying is done based on the difference to the original center, which now holds due to explicit center points
acad.model.Copy(pile1, pile2_center - pile1.Center)
acad.model.Copy(pile1, pile3_center - pile1.Center)
acad.model.Copy(pile1, pile4_center - pile1.Center)

# Dimensioning the pile cap - No direct 'Dimension' command in the API, using AddDimAligned
# For each side of the square
dim1 = acad.model.AddDimAligned(p1, p2, p2 + APoint(0, -100))
dim2 = acad.model.AddDimAligned(p2, p3, p3 + APoint(100, 0))
dim3 = acad.model.AddDimAligned(p4, p3, p3 + APoint(0, 100))
dim4 = acad.model.AddDimAligned(p1, p4, p4 - APoint(100, 0))

# Using AddDimAligned for center-to-center spacing between piles
dim_center_1_2 = acad.model.AddDimAligned(pile1.Center, pile2.Center, pile2.Center + APoint(0, -150))
dim_center_1_3 = acad.model.AddDimAligned(pile1.Center, pile3.Center, pile3.Center - APoint(150, 0))

# Changing the dimension line to a dotted line is not directly supported by pyAutoCAD automation interface
# This typically requires accessing the properties panel which is a manual operation in AutoCAD environment
# You might consider setting the property through the AutoCAD UI or using ObjectARX/COM API if automation is essential