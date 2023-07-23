import math
from tkinter import *



def distance(x1, y1, x2, y2):
    """Function to find length of line between two points"""
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    return d


def areaTriangle(x1, y1, x2, y2, x3, y3):
    """Function to find area of triangle using Heron's formula"""
    a = distance(x1, y1, x2, y2)

    b= distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    s = (a + b + c) / 2

    area= math.sqrt(s*(s-a)*(s-b)*(s-c))

    return area


X1 = int(input("Please enter coordinate x1: "))
Y1 = int(input("Please enter coordinate y1: "))

X2 = int(input("Please enter coordinatex2: "))

Y2 =int(input("Please enter coordinate y2: "))
X3 = int(input("Please enter coordinate x3: "))
Y3 = int(input("Please enter coordinate y3: "))

frame = Tk()
canvas = Canvas(height=350, width=300)
canvas.pack()

canvas.create_line(X1, Y1, X2, Y2)
canvas.create_line(X1, Y1, X3, Y3)
canvas.create_line(X2, Y2, X3, Y3)


area_label = Label(frame, text='Area={}'.format(areaTriangle(X1,Y1,X2,Y2,X3,Y3)))
area_label.pack()


frame.mainloop()
