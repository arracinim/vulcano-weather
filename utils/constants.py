from models.coordinates import Coordinates
import os

# geometry
circumference_degrees = 360.0
sun_coordinates = Coordinates(x=0.0, y=0.0)

# Max triangle perimeter is when the two points with the highest radius
# are in opposite positions so the hypotenuse is the distance between this
# two points are maximum, in this case this perimeter is 6179

max_triangle_perimeter = 6179

# days
ferengi_year_days = 360
ten_years = ferengi_year_days * 10


