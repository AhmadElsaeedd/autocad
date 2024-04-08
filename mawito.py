from pyautocad import Autocad, APoint

# Create Autocad object
acad = Autocad()

# 1 - 6. Draw the square
first_point = APoint(0, 0)
second_point = APoint(2700, 0)
third_point = APoint(2700, 2700)
fourth_point = APoint(0, 2700)
acad.model.AddLine(first_point, second_point)
acad.model.AddLine(second_point, third_point)
acad.model.AddLine(third_point, fourth_point)
acad.model.AddLine(fourth_point, first_point)

# 7 - 10. Draw the piles
centers = [APoint(1350, 1350), APoint(2000, 2000), APoint(2000, 700), APoint(700, 2000), APoint(700, 700)]
for center in centers:
    acad.model.AddCircle(center, 250)

# 11. Add linear dimensions to the pile cap
for i in range(4):
    acad.model.AddDimLinear(first_point, second_point, first_point - APoint(100, 100))

# 12 - 14. Add aligned dimensions between the piles
for i in range(len(centers) - 1):
    dim = acad.model.AddDimAligned(centers[i], centers[i+1], centers[i] - APoint(200, 200))
    dim.Linetype = 'Dotted'