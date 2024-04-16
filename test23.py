from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

# Draw the lines for Room 1
acad.model.AddLine(APoint(0, 0), APoint(12, 0))
acad.model.AddLine(APoint(12, 0), APoint(12, 10))
acad.model.AddLine(APoint(12, 10), APoint(0, 10))
acad.model.AddLine(APoint(0, 10), APoint(0, 0))

# Draw the lines for Room 2
acad.model.AddLine(APoint(12, 0), APoint(32, 0))
acad.model.AddLine(APoint(32, 0), APoint(32, 18))
acad.model.AddLine(APoint(32, 18), APoint(12, 18))
acad.model.AddLine(APoint(12, 18), APoint(12, 10))

# Add the text labels for each room
acad.model.AddText("Room 1", APoint(6, 5), 2)  # Room 1 label
acad.model.AddText("Room 2", APoint(22, 9), 2) # Room 2 label