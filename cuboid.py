from __future__ import annotations
import numpy as np
from tkinter import Canvas


class Cuboid:
    
    def __init__(self, x, y, z, width, height, deepth) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.deepth = deepth
    
    def getPointsCoordinates(self):
        points = []
        points.append(Point3D(self.x, self.y, self.z))
        points.append(Point3D(self.x, self.y + self.height, self.z))
        points.append(Point3D(self.x + self.width, self.y, self.z))
        points.append(Point3D(self.x + self.width, self.y + self.height, self.z))
        points.append(Point3D(self.x, self.y, self.z + self.deepth))
        points.append(Point3D(self.x, self.y + self.height, self.z + self.deepth))
        points.append(Point3D(self.x + self.width, self.y, self.z + self.deepth))
        points.append(Point3D(self.x + self.width, self.y + self.height, self.z + self.deepth))
        return points
    
    def getPointsInVectors(self) -> list[np.ndarray]:
        points = []
        points.append(np.array([[self.x, self.y, self.z, 1]]).T)
        points.append(np.array([[self.x, self.y + self.height, self.z, 1]]).T)
        points.append(np.array([[self.x + self.width, self.y, self.z, 1]]).T)
        points.append(np.array([[self.x + self.width, self.y + self.height, self.z, 1]]).T)
        points.append(np.array([[self.x, self.y, self.z + self.deepth, 1]]).T)
        points.append(np.array([[self.x, self.y + self.height, self.z + self.deepth, 1]]).T)
        points.append(np.array([[self.x + self.width, self.y, self.z + self.deepth, 1]]).T)
        points.append(np.array([[self.x + self.width, self.y + self.height, self.z + self.deepth, 1]]).T)
        return points
    
    
    def project(self, projection:np.ndarray) -> list[Point3D]:
        points = self.getPointsCoordinates()
        projected_points = []
        for point in points:
            projected_points.append(point.projectToPoint3D(projection))
        return projected_points
    

    
    def __str__(self) -> str:
        tmp = ""
        points = self.getPointsCoordinates()
        for point in points:
            tmp += str(point) + '\n'
        return tmp
    
    def projectAndDraw(self, projection:np.ndarray, canvas:Canvas, canvas_height, canvas_width, color='black', line_width=1):
        pp = [] # projected_points
        for p in self.getPointsInVectors():
            tmp = projection.dot(p)
            tmp = tmp/(tmp[3][0])
            tmp[0][0] = (tmp[0][0] * canvas_width/2) + canvas_width/2
            tmp[1][0] = (-tmp[1][0] * canvas_height/2) + canvas_height/2
            pp.append(tmp)
        
        canvas.create_line(pp[0][0][0], pp[0][1][0], pp[1][0][0], pp[1][1][0], fill=color, width=line_width)
        canvas.create_line(pp[0][0][0], pp[0][1][0], pp[2][0][0], pp[2][1][0], fill=color, width=line_width)
        canvas.create_line(pp[3][0][0], pp[3][1][0], pp[1][0][0], pp[1][1][0], fill=color, width=line_width)
        canvas.create_line(pp[3][0][0], pp[3][1][0], pp[2][0][0], pp[2][1][0], fill=color, width=line_width)
        canvas.create_line(pp[0][0][0], pp[0][1][0], pp[4][0][0], pp[4][1][0], fill=color, width=line_width)
        canvas.create_line(pp[1][0][0], pp[1][1][0], pp[5][0][0], pp[5][1][0], fill=color, width=line_width)
        canvas.create_line(pp[2][0][0], pp[2][1][0], pp[6][0][0], pp[6][1][0], fill=color, width=line_width)
        canvas.create_line(pp[3][0][0], pp[3][1][0], pp[7][0][0], pp[7][1][0], fill=color, width=line_width)
        canvas.create_line(pp[4][0][0], pp[4][1][0], pp[5][0][0], pp[5][1][0], fill=color, width=line_width)
        canvas.create_line(pp[4][0][0], pp[4][1][0], pp[6][0][0], pp[6][1][0], fill=color, width=line_width)
        canvas.create_line(pp[7][0][0], pp[7][1][0], pp[5][0][0], pp[5][1][0], fill=color, width=line_width)
        canvas.create_line(pp[7][0][0], pp[7][1][0], pp[6][0][0], pp[6][1][0], fill=color, width=line_width)
        print('done')
        
        
    
        
    
    
class Point3D:
    def __init__(self,x:float,y:float,z:float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = 1
    
    
    
    def __str__(self) -> str:
        return str(self.x) + " " + str(self.y) + " " + str(self.z)
    
    def toArray(self):
        return np.array([[self.x, self.y, self.z, self.w]]).T
    
    def fromArray(self, array:np.ndarray):
        self.x = float(array[0][0])
        self.y = float(array[1][0])
        self.z = float(array[2][0])
        self.w = float(array[3][0])

    
    def project(self, projection_matrix:np.ndarray):
        p = self.toArray()
        r = projection_matrix.dot(p)
        w = r[3][0]
        return r/w
    
    def projectToPoint3D(self, projection_matrix:np.ndarray) -> Point3D:
        p = self.toArray()
        r = projection_matrix.dot(p)
        w = r[3][0]
        P = Point3D(1,1,1)
        print(r/w)
        P.fromArray(r/w)
        return P
        