import tkinter as tk
import cuboid as c
from scene import Scene

WIDTH = 800
HEIGHT = 800

window  = tk.Tk()
window.geometry("" + str(WIDTH) + "x" + str(HEIGHT))

canvas = tk.Canvas(window, bg='grey', width=WIDTH, height=HEIGHT)
canvas.pack()

c1 = c.Cuboid(10, -20, 50, 20,20,20)
c2 = c.Cuboid(-20, -20, 40, 20,30,40)
c3 = c.Cuboid(10, -20, 80, 50,40,20)
c4 = c.Cuboid(-20, -20, 100, 20,20,20)

scene = Scene([c1,c2,c3,c4], canvas, HEIGHT, WIDTH)
scene.render()

def mv_up(event):
    pass

def mv_down(event):
    pass

def mv_left(event):
    pass

def mv_right(event):
    pass

def mv_front(event):
    pass

def mv_back(event):
    pass

window.bind('<Up>', mv_up)
window.bind('<Down>', mv_down)
window.bind('<Left>', mv_left)
window.bind('<Right>', mv_right)
window.bind('z', mv_front)
window.bind('x', mv_back)


window.mainloop()
