# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:14:20 2020

@author: nschildberg
"""

from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()