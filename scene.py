from cuboid import Cuboid
from tkinter import Canvas
from math import pi
from transformations import *

class Scene():
    
    def __init__(self, cuboids: list[Cuboid], canvas: Canvas, canvas_height:int, canvas_width:int) -> None:
        self.cuboids = cuboids
        self.canvas = canvas
        
        self.fov = pi/2
        self.cam_height = canvas_height
        self.cam_width = canvas_width
        self.near_plane_distance = 1
        self.far_plane_distance = 200
        
        self.updateProjectionMatrix()
        
        
    def updateProjectionMatrix(self):
        self.projection_matrix = perspectiveProjectionMatrix(self.cam_width,
                                                             self.cam_height,
                                                             self.fov,
                                                             self.near_plane_distance,
                                                             self.far_plane_distance)
        
        
    def render(self):
        for c in self.cuboids:
            c.projectAndDraw(self.projection_matrix, self.canvas, self.cam_height, self.cam_width)
    
    
        