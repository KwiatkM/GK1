from cuboid import Cuboid, Point3D
from transformations import perspectiveProjectionMatrix
from math import pi

a = Cuboid(10, 20, 50, 20,20,20)
print(a.getPointsInVectors())

#P = a.getPointsCoordinates()[0]
#p = P.toArray()
#print(p)
#projection = perspectiveProjectionMatrix(1000, 1000, pi/2, 1, 100)
#print(P.project(projection))

