from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)

# Draw pentagonal outline
# Top line
p1 = APoint(0, 0)
p2 = APoint(800, 0)
acad.model.AddLine(p1, p2)

# 1250 mm lines at 60 degrees
angle_60_rad = math.radians(60)
p3 = APoint(800 + 1250 * math.cos(angle_60_rad), 1250 * math.sin(angle_60_rad))
p4 = APoint(-1250 * math.cos(angle_60_rad), 1250 * math.sin(angle_60_rad))
acad.model.AddLine(p2, p3)
acad.model.AddLine(p1, p4)

# 750 mm side lines
p5 = APoint(800 + 1250 * math.cos(angle_60_rad) - 750, 1250 * math.sin(angle_60_rad))
p6 = APoint(-1250 * math.cos(angle_60_rad) + 750, 1250 * math.sin(angle_60_rad))
acad.model.AddLine(p3, p5)
acad.model.AddLine(p4, p6)

# Line to close the pentagon
acad.model.AddLine(p5, p6)

# Draw circular piles
center_x1 = 400
center_y1 = 1250 * math.sin(angle_60_rad) / 3
center_x2 = 400 - 625 * math.cos(angle_60_rad)
center_y2 = center_y1 - 625 * math.sin(angle_60_rad)
center_x3 = 400 + 625 * math.cos(angle_60_rad)
center_y3 = center_y2

# Pile circles
radius = 250
acad.model.AddCircle(APoint(center_x1, center_y1), radius)
acad.model.AddCircle(APoint(center_x2, center_y2), radius)
acad.model.AddCircle(APoint(center_x3, center_y3), radius)