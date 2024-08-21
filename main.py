from tkinter import *
from tkinter import ttk
from mandelbrot import create_mandelbrot_image
from PIL import ImageTk, Image

WIDTH = 800
HEIGHT = 600
REVOLUTIONS = 200
ZOOM = 0.005
ZOOM_ON_CLICK = 0.2
OFFSET = (-0.8, 0)

offsets = []

level = -1

def zoom_on_click(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
    global OFFSET
    global ZOOM
    new_offset = (OFFSET[0] + (x-(WIDTH/2))*ZOOM,
                  OFFSET[1] + (y-(HEIGHT/2))*ZOOM)
    OFFSET = new_offset
    ZOOM *= ZOOM_ON_CLICK
    draw_mandelbrot()

def zoom_out(eventorigin):
    global level
    global OFFSET
    global ZOOM
    if level > 0:
        level -= 1
        ZOOM *= 1/ZOOM_ON_CLICK
        OFFSET = offsets[level]
        img = PhotoImage(file=f"images/image{level}.png")
        label.configure(image=img)
        label.image = img

def draw_mandelbrot():
    global level
    tmp_img = create_mandelbrot_image((WIDTH, HEIGHT), REVOLUTIONS, ZOOM, OFFSET)
    level += 1
    if len(offsets) <= level:
        offsets.append(OFFSET)
    else:
        offsets[level] = OFFSET
    tmp_img.save(f"images/image{level}.png", "PNG")
    img = ImageTk.PhotoImage(tmp_img)
    label.configure(image=img)
    label.image = img

root = Tk()
root.title("Mandelbrot")
root.resizable(False,False)

label = Label(root)
label.pack()

draw_mandelbrot()


label.bind("<Button 1>", zoom_on_click)
root.bind("<Button 3>", zoom_out)

root.mainloop()