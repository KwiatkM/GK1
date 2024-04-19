from cuboid import Cuboid, Point3D
from transformations import perspectiveProjectionMatrix
from math import pi

projection = perspectiveProjectionMatrix(1000, 1000, pi/2, 1, 100)

a = Cuboid(10, 20, 50, 20,20,20)
points = a.getPointsCoordinates()

P = points[0].projectToPoint3D(projection)
t = points[0].project(projection)
print(points[0])
print(type(P))
print(P)
