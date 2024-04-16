from pyautocad import Autocad, APoint
from math import cos, sin, radians

acad = Autocad(create_if_not_exists=True)

# Lines
acad.model.AddLine(APoint(0, 0), APoint(2050, 0))
acad.model.AddLine(APoint(2050, 0), APoint(2050, 750))
acad.model.AddLine(APoint(0, 0), APoint(0, 750))
acad.model.AddLine(APoint(2050, 750), APoint(2050 + 1250 * cos(radians(150)), 750 + 1250 * sin(radians(150))))
acad.model.AddLine(APoint(0, 750), APoint(0 + 1250 * cos(radians(30)), 750 + 1250 * sin(radians(30))))
acad.model.AddLine(APoint(0 + 1250 * cos(radians(30)), 750 + 1250 * sin(radians(30))), APoint(2050 + 1250 * cos(radians(150)), 750 + 1250 * sin(radians(150))))

# Circles
acad.model.AddCircle(APoint(625, 375), 250)
acad.model.AddCircle(APoint(1250, 375), 250)
acad.model.AddCircle(APoint(1875, 375), 250)