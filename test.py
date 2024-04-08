from pyautocad import Autocad, APoint

# Creating Autocad object
acad = Autocad(create_if_not_exists=True)

# Using the ModelSpace
model = acad.model

# Creating square
p1 = APoint(0,0)
p2 = APoint(2700,0)
p3 = APoint(2700,2700)
p4 = APoint(0,2700)

model.add_line(p1, p2)
model.add_line(p2, p3)
model.add_line(p3, p4)
model.add_line(p4, p1)

# Creating piles
pile_centers = [APoint(625,625), APoint(625,2075), APoint(2075,625), APoint(2075,2075)]

for center in pile_centers:
    model.add_circle(center, 250)