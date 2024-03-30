import tkinter as tk

# window setup
window  = tk.Tk()
window.geometry('600x600')

def color_pixel(event):
    x = event.x
    y = event.y
    canvas.create_oval((x-2, y-2, x+2, y+2), fill='black')
    

canvas = tk.Canvas(window, bg='grey', width=600, height=600)
canvas.bind('<Motion>', color_pixel)
window.bind('')
canvas.pack()


    




window.mainloop()