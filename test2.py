import tkinter as tk
import numpy as np
from math import pi, cos, sin

window  = tk.Tk()
window.geometry('1000x1000')

p = np.array([[200,200]]).T

angle = -pi/45
rotation_matrix = np.array([[cos(angle), -sin(angle)],
                           [sin(angle), cos(angle)]])


canvas = tk.Canvas(window, bg='grey', width=1000, height=1000)
for i in range(10):
    canvas.create_oval((p[0][0],p[1][0],p[0][0] + 10,p[1][0] + 10), fill='black')
    p = rotation_matrix.dot(p)
canvas.pack()



window.mainloop()

