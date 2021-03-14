from tkinter import *
import math
from random import randint
from time import sleep
WIDTH = 800
HEIGHT = 800
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/8
lastKnownCursor = [0,0]
root = Tk()
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()

vertices = [
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y + SIDE/2],
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y + SIDE/2],
]

def rotate(points, angle, center):
    moved_points = updatePosition(center)  

    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in moved_points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points

def draw_square(points, color="red"):
    canvas.delete("all")
    canvas.create_polygon(points, fill=color)

def updateDirection(event):
    global center,lastKnownCursor
    if event == "DIRECTION":
        x = lastKnownCursor[0]
        y = lastKnownCursor[1]
    else:
        x, y = event.x, event.y
        lastKnownCursor = [x,y]
        
    X = center[0]
    Y = center[1]

    if (abs(y-Y) != 0) and (abs(x-X) != 0):
        if ((x > X) and (Y > y)) or ((X > x) and (y > Y)):
            angle = - math.degrees(math.atan( (abs(y-Y) / abs(x-X)) ))
        else:
            angle = math.degrees(math.atan( (abs(y-Y) / abs(x-X)) ))   
    
        new_square = rotate(vertices, angle, center)
        draw_square(new_square)
        canvas.create_line(X,Y,x,y, fill="blue")
        angleOld = angle

def updatePosition(center):
    moved_points = []
    moved_points.append([center[0]-SIDE,center[1]-SIDE])
    moved_points.append([center[0]-SIDE,center[1]+SIDE])
    moved_points.append([center[0]+SIDE,center[1]+SIDE])
    moved_points.append([center[0]+SIDE,center[1]-SIDE])
    return(moved_points)

def move(letter):
    global center,lastKnownCursor
    if letter == "w":
        center = [center[0],center[1]-10]
    elif letter == "s":
        center = [center[0],center[1]+10]
    elif letter == "a":
        center = [center[0]-10,center[1]]
    elif letter == "d":
        center = [center[0]+10,center[1]]

    updateDirection("DIRECTION")

        
center = (CANVAS_MID_X, CANVAS_MID_Y)
center = (400.0,400.0)
new_square = rotate(vertices, 0, center)
draw_square(new_square)
root.bind('<Motion>', updateDirection)
root.bind('w', lambda x: move('w'))
root.bind('s', lambda x: move('s'))
root.bind('a', lambda x: move('a'))
root.bind('d', lambda x: move('d'))

#root.update()
#angle=180
#while True:
#    angle = input("Enter Angle\n")
#    print(angle)
#    new_square = rotate(vertices, float(angle), center)
#    draw_square(new_square)
#    root.update()

mainloop()
