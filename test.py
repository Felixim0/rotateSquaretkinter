from tkinter import *
x_vel = 0
y_vel = 0
x = 10
y = 10
a = 100
b = 100
direction = None

def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        canvas1.move(rect, x_vel,y_vel)
    window.after(3,move)

def on_keypress( event ):                          # keeping the Globals-style,
    global direction                               #         however shall be rather
    global x_vel                                   #         implemented in a Class-based
    global y_vel                                   #         manner

    direction     = dir_vel[event.keysym][0]       # ref. remark on more complex FSA
    x_vel        += dir_vel[event.keysym][1]
    y_vel        += dir_vel[event.keysym][2]

def on_keyrelease( event ):
    global direction
    global x_vel
    global y_vel
    x_vel        -= dir_vel[event.keysym][1]
    y_vel        -= dir_vel[event.keysym][2]
    if abs( x_vel * y_vel ) < 0.1:
        direction = None                          # ref. remark on more complex FSA

dir_vel = {
    "Left": ("left", -5, 0),
    "Right": ('right', 5, 0),
    "Down": ('down', 0, 5),
    "Up": ('up', 0, -5),}


window = Tk()
window.geometry("900x900")

move()

#canvas and drawing
canvas1=Canvas(window, height = 900, width = 900)
canvas1.grid(row=0, column=0, sticky=W)
coord = [x, y, a, b]
rect = canvas1.create_rectangle(*coord, outline="#fb0", fill="#fb0")

#capturing keyboard inputs and assigning to function
window.bind_all('<KeyPress>', on_keypress)
window.bind_all('<KeyRelease>', on_keyrelease)
