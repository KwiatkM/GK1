from __future__ import annotations
import numpy as np
from tkinter import Canvas


class Cuboid:
    
    def __init__(self, x, y, z, width, height, deepth) -> None:
        #self.x = x
        #self.y = y
        #self.z = z
        #self.width = width
        #self.height = height
        #self.deepth = deepth
        self.ppn = [] #projected_points_normalized
        self.pp = [] #projected points in canvas coordinates
        self.points = []
        self.points.append(np.array([[x, y, z, 1]]).T)
        self.points.append(np.array([[x, y + height, z, 1]]).T)
        self.points.append(np.array([[x + width, y, z, 1]]).T)
        self.points.append(np.array([[x + width, y + height, z, 1]]).T)
        self.points.append(np.array([[x, y, z + deepth, 1]]).T)
        self.points.append(np.array([[x, y + height, z + deepth, 1]]).T)
        self.points.append(np.array([[x + width, y, z + deepth, 1]]).T)
        self.points.append(np.array([[x + width, y + height, z + deepth, 1]]).T)


    
    def __str__(self) -> str:
        tmp = ""
        points = self.getPointsCoordinates()
        for point in points:
            tmp += str(point) + '\n'
        return tmp
    
    def projectAndDraw(self, projection:np.ndarray, canvas:Canvas, canvas_height, canvas_width, color='black', line_width=1):
        pp = [] # projected_points
        ppn = [] # projected_points_normalized
        for p in self.points:
            tmp = projection.dot(p)

            if tmp[3][0] == 0: 
                tmp = np.array([[float('inf'), float('inf'), float('inf'), 1]]).T
            else:
                tmp = tmp/(tmp[3][0])
        
            

            ppn.append(tmp)
            tmp[0][0] = (tmp[0][0] * canvas_width/2) + canvas_width/2
            tmp[1][0] = (-tmp[1][0] * canvas_height/2) + canvas_height/2
            pp.append(tmp)
        self.ppn = ppn
        self.pp = pp
        
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


    def applyTransformation(self, transformation:np.ndarray):
        for i, point in enumerate(self.points):
            tmp = transformation.dot(point)
            tmp = tmp/(tmp[3][0])
            self.points[i] = tmp

        