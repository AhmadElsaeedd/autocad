from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

# Define start points
start_points = [APoint(0, 0), APoint(12, 0), APoint(12, 10), APoint(0, 10),
                APoint(12, 0), APoint(32, 0), APoint(32, 18), APoint(12, 18)]

# Define end points based on calculations
end_points = [APoint(12, 0), APoint(12, 10), APoint(0, 10), APoint(0, 0),
              APoint(32, 0), APoint(32, 18), APoint(12, 18), APoint(12, 10)]

# Draw lines
for start, end in zip(start_points, end_points):
    acad.model.AddLine(start, end)