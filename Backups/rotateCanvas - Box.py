
def updateDirection(event):
    x, y = event.x, event.y
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

from tkinter import *
import math
from random import randint
from time import sleep
WIDTH = 400
HEIGHT = 400
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/4

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
    angle = math.radians(angle)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    cx, cy = center
    new_points = []
    for x_old, y_old in points:
        x_old -= cx
        y_old -= cy
        x_new = x_old * cos_val - y_old * sin_val
        y_new = x_old * sin_val + y_old * cos_val
        new_points.append([x_new + cx, y_new + cy])
    return new_points

def draw_square(points, color="red"):
    canvas.delete("all")
    canvas.create_polygon(points, fill=color)

def test():
    old_vertices = [[150, 150], [250, 150], [250, 250], [150, 250]]
    print ("vertices: ", vertices, "should be: ", old_vertices)
    print (vertices == old_vertices)

draw_square(vertices, "blue")

center = (CANVAS_MID_X, CANVAS_MID_Y)
new_square = rotate(vertices, 30, center)
#test()
draw_square(new_square)
root.bind('<Motion>', updateDirection)

#root.update()
#angle=180
#while True:
#    angle = input("Enter Angle\n")
#    print(angle)
#    new_square = rotate(vertices, float(angle), center)
#    draw_square(new_square)
#    root.update()

mainloop()
