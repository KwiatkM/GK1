import tkinter as tk
import numpy as np
from math import pi, cos, sin
from cuboid import Cuboid, Point3D
from transformations import perspectiveProjectionMatrix

window  = tk.Tk()
WIDTH = 800
HEIGHT = 800
window.geometry("" + str(WIDTH) + "x" + str(HEIGHT))

global fov
fov = pi/2
projection = perspectiveProjectionMatrix(WIDTH, HEIGHT, fov, 30, 100)

a = Cuboid(10, 20, 50, 20,20,20)
points = a.getPointsCoordinates()
proj = a.project(projection)

canvas = tk.Canvas(window, bg='grey', width=WIDTH, height=HEIGHT)
canvas.pack()

#for point in points:
#    canvas.create_oval((point.x + WIDTH/2 ,-point.y + HEIGHT/2, point.x + WIDTH/2 + 5 ,-point.y + HEIGHT/2 + 5), fill='black')
    
for p in proj:
    canvas.create_oval(((p.x * WIDTH/2) + WIDTH/2 ,(-p.y * HEIGHT/2) + HEIGHT/2, (p.x * WIDTH/2) + WIDTH/2 + 10 ,(-p.y * HEIGHT/2) + HEIGHT/2 + 10), fill='red')

canvas.create_line((proj[0].x * WIDTH/2) + WIDTH/2 , (-proj[0].y * HEIGHT/2) + HEIGHT/2,
                   (proj[1].x * WIDTH/2) + WIDTH/2 , (-proj[1].y * HEIGHT/2) + HEIGHT/2, width=2, fill='red')
canvas.create_line((proj[0].x * WIDTH/2) + WIDTH/2 , (-proj[0].y * HEIGHT/2) + HEIGHT/2,
                   (proj[2].x * WIDTH/2) + WIDTH/2 , (-proj[2].y * HEIGHT/2) + HEIGHT/2, width=2, fill='red')
canvas.create_line((proj[0].x * WIDTH/2) + WIDTH/2 , (-proj[0].y * HEIGHT/2) + HEIGHT/2,
                   (proj[4].x * WIDTH/2) + WIDTH/2 , (-proj[4].y * HEIGHT/2) + HEIGHT/2, width=2, fill='red')

def refresh(projection = projection):
    #points = a.getPointsCoordinates()
    proj = a.project(projection)
    canvas.delete("all")
    for p in proj:
        canvas.create_oval(((p.x * WIDTH/2) + WIDTH/2 ,(-p.y * HEIGHT/2) + HEIGHT/2, (p.x * WIDTH/2) + WIDTH/2 + 10 ,(-p.y * HEIGHT/2) + HEIGHT/2 + 10), fill='red')

    canvas.create_line((proj[0].x * WIDTH/2) + WIDTH/2 , (-proj[0].y * HEIGHT/2) + HEIGHT/2,
                   (proj[1].x * WIDTH/2) + WIDTH/2 , (-proj[1].y * HEIGHT/2) + HEIGHT/2, width=2, fill='red')
    canvas.create_line((proj[0].x * WIDTH/2) + WIDTH/2 , (-proj[0].y * HEIGHT/2) + HEIGHT/2,
                   (proj[2].x * WIDTH/2) + WIDTH/2 , (-proj[2].y * HEIGHT/2) + HEIGHT/2, width=2, fill='red')
    canvas.create_line((proj[0].x * WIDTH/2) + WIDTH/2 , (-proj[0].y * HEIGHT/2) + HEIGHT/2,
                   (proj[4].x * WIDTH/2) + WIDTH/2 , (-proj[4].y * HEIGHT/2) + HEIGHT/2, width=2, fill='red')
    print('=======')

def change_z_up(event):
    a.z += 5
    refresh()

def change_z_down(event):
    a.z -= 5
    refresh()

def change_x_up(event):
    a.x += 5
    refresh()

def change_x_down(event):
    a.x -= 5
    refresh()

def change_y_up(event):
    a.y += 5
    refresh()

def change_y_down(event):
    a.y -= 5
    refresh()

def fov_up(event):
    global fov
    fov += pi/36
    
    refresh(projection=perspectiveProjectionMatrix(WIDTH, HEIGHT, fov, 30, 100))
    


window.bind('<Up>', change_z_up)
window.bind('<Down>', change_z_down)
window.bind('w', change_y_up)
window.bind('s', change_y_down)
window.bind('a', change_x_up)
window.bind('d', change_x_down)
window.bind('z', fov_up)




window.mainloop()
