from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)

# Drawing the hexagonal outline
# Top horizontal line
acad.model.AddLine(APoint(0, 0), APoint(800, 0))

# Upper right side
p1 = APoint(800, 0)
print("P1 x is: ", p1.x)
print("P1 x is: ", p1.y)
p2 = APoint(800 + (1250 * math.sin(math.radians(30))), -1250 * math.cos(math.radians(30)))
acad.model.AddLine(p1, p2)

# Lower right side
print(p2.x)
print(p2.y)
p3 = APoint(p2.x+(750 * math.sin(math.radians(180))), p2.y + (-750 * math.sin(math.radians(90))))
acad.model.AddLine(p2, p3)

# Bottom horizontal line
p4 = APoint(p3.x - 2050, p3.y)
acad.model.AddLine(p3, p4)

# Lower left side
p5 = APoint(p4.x + (750 * math.cos(math.radians(90))), p4.y + (750 * math.sin(math.radians(90))))
acad.model.AddLine(p4, p5)

# Upper left side to close the hexagon
acad.model.AddLine(p5, APoint(0, 0))

# Adding the three circular piles
# First circle
acad.model.AddCircle(APoint(0, 0), 250)

# Second circle
acad.model.AddCircle(APoint(1250, 0), 250)

# Third circle
acad.model.AddCircle(APoint(2500, 0), 250)

# Adding dimensions (Points for dimensioning are adjusted manually)
# Top horizontal line dimension
# acad.model.AddDimAligned(APoint(0, 0), APoint(800, 0), APoint(400, -100))

# # Upper right side dimension
# acad.model.AddDimAligned(p1, p2, APoint(p2.x - 50, p2.y - 50))

# # Lower right side dimension
# acad.model.AddDimAligned(p2, p3, APoint(p3.x - 100, p3.y - 10))

# # Bottom horizontal line dimension
# acad.model.AddDimAligned(p3, p4, APoint(p3.x - 1025, p3.y - 100))

# # Lower left side dimension
# acad.model.AddDimAligned(p4, p5, APoint(p5.x - 100, p5.y - 100))

# # Upper left side dimension
# acad.model.AddDimAligned(APoint(0, 0), p5, APoint(-100, p5.y / 2))

# # Dimensions for the center-to-center spacing between the circular piles
# acad.model.AddDimAligned(APoint(0, 0), APoint(1250, 0), APoint(625, 300))
# acad.model.AddDimAligned(APoint(1250, 0), APoint(2500, 0), APoint(1875, 300))