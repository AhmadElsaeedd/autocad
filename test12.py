from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

# Outer perimeter
acad.model.AddLine(APoint(0, 0), APoint(25.25, 0))
acad.model.AddLine(APoint(0, 0), APoint(0, 35.75))
acad.model.AddLine(APoint(0, 35.75), APoint(21.75, 35.75))
acad.model.AddLine(APoint(21.75, 35.75), APoint(21.75, 24.75))
acad.model.AddLine(APoint(21.75, 24.75), APoint(25.25, 24.75))
acad.model.AddLine(APoint(25.25, 24.75), APoint(25.25, 0))

# Internal walls
acad.model.AddLine(APoint(0, 32.75), APoint(0, 28.75))
acad.model.AddLine(APoint(0, 28.75), APoint(13.5, 28.75))

# Stair representation
acad.model.AddLine(APoint(3, 35.75), APoint(3, 33.75))
acad.model.AddLine(APoint(3, 33.75), APoint(2, 33.25))
acad.model.AddLine(APoint(2, 33.25), APoint(3, 32.75))

# Room labels
acad.model.AddText("BEDROOM 13'-6\"x10'", APoint(10.5, 30.75), 2)
acad.model.AddText("BATH 11'x8'", APoint(17.75, 27.75), 2)
acad.model.AddText("DINING 11'x14'", APoint(18.25, 21.75), 2)
acad.model.AddText("DRAWING 12'x18'", APoint(6.5, 17.75), 2)

# Dimensions
# Note: Since Dimension method is not directly available, AddDimension could be a placeholder
# for the specialized dimension functions available in AutoCAD via ActiveX. Detailed dimensioning
# would require using the specific dimensioning functions as per the AutoCAD ActiveX documentation.

# Placeholder for dimensioning
# acad.model.AddDimension(APoint(0, -1), APoint(25.25, -1), APoint(0,0), 0)
# acad.model.AddDimension(APoint(-1, 0), APoint(-1, 35.75), APoint(0,0), 90)