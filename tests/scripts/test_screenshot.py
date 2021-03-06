#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:10:32 2020

@author: chujiechen
"""

import tkinter as tk
from PIL import Image, ImageTk

WIDTH, HEIGHT = 900, 900
topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None
path = "../images/phototest-original.png"


def get_mouse_posn(event):
    global topy, topx
    
    topx, topy = event.x, event.y

def update_sel_rect(event):
    global rect_id
    global topy, topx, botx, boty

    botx, boty = event.x, event.y
    canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.
    # print(topx, topy)
    # print(botx, boty)


window = tk.Tk()
window.title("Select Area")
window.geometry('%sx%s' % (WIDTH, HEIGHT))
window.configure(background='grey')

img = ImageTk.PhotoImage(Image.open(path))
canvas = tk.Canvas(window, width=img.width(), height=img.height(),
                   borderwidth=0, highlightthickness=0)
canvas.pack(expand=True)
canvas.img = img  # Keep reference in case this code is put into a function.
canvas.create_image(0, 0, image=img, anchor=tk.NW)

# Create selection rectangle (invisible since corner points are equal).
rect_id = canvas.create_rectangle(topx, topy, topx, topy,
                                  dash=(4,4), fill='', outline='red',width=2.0)

canvas.bind('<Button-1>', get_mouse_posn)
canvas.bind('<B1-Motion>', update_sel_rect)

window.mainloop()