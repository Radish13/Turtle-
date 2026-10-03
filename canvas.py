import turtle
import tkinter as tk
from tkinter import colorchooser
import math

screen = turtle.Screen()
screen.title("Turtle CAD - Polyline Offset Trim")
screen.setup(700, 600)
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

canvas = screen.getcanvas()
root = canvas.master

polyline_points = [] # store points for polyline
polyline_mode = False
lines = [] # store all drawn lines: [(x1,y1,x2,y2)]

def forward(): t.forward(20)
def back(): t.backward(20)
def left(): t.left(15)
def right(): t.right(15)
def pen_up(): t.penup()
def pen_down(): t.pendown()
def clear():
    global lines, polyline_points
    t.clear(); t.home()
    lines = []; polyline_points = []

def size_small(): t.pensize(1)
def size_medium(): t.pensize(3)
def size_big(): t.pensize(6)

def pick_color():
    color = colorchooser.askcolor()[1]
    if color: t.color(color)

# 1. POLYLINE: click points to connect
def toggle_polyline():
    global polyline_mode, polyline_points
    polyline_mode = not polyline_mode
    polyline_points = []
    poly_btn.config(text="Polyline ON" if polyline_mode else "Polyline")
    if not polyline_mode: polyline_points = []

def add_polyline_point(x, y):
    global polyline_points
    if not polyline_mode: return
    polyline_points.append((x,y))
    t.goto(x,y)
    if len(polyline_points) > 1:
        x1,y1 = polyline_points[-2]
        x2,y2 = polyline_points[-1]
        lines.append((x1,y1,x2,y2))

def finish_polyline():
    global polyline_mode, polyline_points
    polyline_mode = False
    polyline_points = []
    poly_btn.config(text="Polyline")

# 2. OFFSET: offset last line by distance
def offset_last(distance=20):
    if not lines: return
    x1,y1,x2,y2 = lines[-1]
    # get perpendicular vector
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0: return
    # unit perpendicular
    nx = -dy / length
    ny = dx / length
    # offset
    ox1, oy1 = x1 + nx*distance, y1 + ny*distance
    ox2, oy2 = x2 + nx*distance, y2 + ny*distance

    t.penup(); t.goto(ox1, oy1); t.pendown()
    t.goto(ox2, oy2)
    lines.append((ox1,oy1,ox2,oy2))

# 3. TRIM: trim last 2 lines at intersection
def line_intersect(l1, l2):
    x1,y1,x2,y2 = l1
    x3,y3,x4,y4 = l2
    den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if den == 0: return None
    px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/den
    py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/den
    return px, py

def trim_last_two():
    if len(lines) < 2: return
    l1 = lines[-2]; l2 = lines[-1]
    ip = line_intersect(l1,l2)
    if not ip: return
    px, py = ip
    # redraw l1 trimmed to intersection
    t.clear()
    for x1,y1,x2,y2 in lines[:-2]:
        t.penup(); t.goto(x1,y1); t.pendown(); t.goto(x2,y2)
    # draw trimmed lines
    t.penup(); t.goto(l1[0],l1[1]); t.pendown(); t.goto(px,py)
    t.penup(); t.goto(l2[0],l2[1]); t.pendown(); t.goto(px,py)
    lines[-2] = (l1[0],l1[1],px,py)
    lines[-1] = (l2[0],l2[1],px,py)

# Click to add polyline points
screen.onclick(add_polyline_point)

# GUI
frame = tk.Frame(root); frame.pack(pady=5)
tk.Button(frame, text="Fwd", command=forward).grid(row=0, column=0)
tk.Button(frame, text="Back", command=back).grid(row=0, column=1)
tk.Button(frame, text="Left", command=left).grid(row=0, column=2)
tk.Button(frame, text="Right", command=right).grid(row=0, column=3)

tk.Button(frame, text="PenUp", command=pen_up).grid(row=1, column=0)
tk.Button(frame, text="PenDown", command=pen_down).grid(row=1, column=1)
tk.Button(frame, text="Clear", bg="yellow", command=clear).grid(row=1, column=2)

tk.Button(frame, text="Thin", command=size_small).grid(row=2, column=0)
tk.Button(frame, text="Medium", command=size_medium).grid(row=2, column=1)
tk.Button(frame, text="Thick", command=size_big).grid(row=2, column=2)
tk.Button(frame, text="Color", command=pick_color).grid(row=2, column=3)

poly_btn = tk.Button(frame, text="Polyline", bg="lightblue", command=toggle_polyline)
poly_btn.grid(row=3, column=0)
tk.Button(frame, text="Finish Poly", command=finish_polyline).grid(row=3, column=1)
tk.Button(frame, text="Offset +20", command=lambda: offset_last(20)).grid(row=3, column=2)
tk.Button(frame, text="Trim Last2", bg="orange", command=trim_last_two).grid(row=3, column=3)

turtle.done()