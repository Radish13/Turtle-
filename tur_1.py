import turtle
import math
import random
t=turtle.Turtle()
t.speed(0)
s=turtle.Screen()

s.bgcolor("black")
s.title("test")
t.pencolor("red")
#t.goto(360,50)
#t.lt(45)
#t.fd(100)
#t.circle(50)
#t.penup()
#t.goto(460,24)
#t.pendown()
#t.circle(44)
#n=1
#while n==0:
#	t.pu()
#	t.goto(45,60)
#	t.pd()
#	for i in range(1,20):
#		t.lt(10)
#		t.fd(12)
#	for j in range(1,5):
#		t.lt(15)
#		for i in range(1,j):
#			t.lt(45)
#			t.fd(20)
#def fun():
#	t.goto(34,65)
#	t.rt(67)
#	t.circle(400,3,5)



#t.pu()
#t.goto(36,65)
#t.pd()
#for i in range(1,5):
#	t.shape("arrow")
#	t.stamp()
#n=8
#u=80
#p=360/n
#for i in range(0,n):
#	t.fd(u)
#	t.rt(p)
#import math
#for i in range(80,800,50):
# # s=math.acos(i)+math.asin(i/2)
#  s=i//2
#  n=['red','blue','brown','pink',"green"]
#  a=random.choice(n)
#  t.fillcolor(a)
#  t.begin_fill()
#  t.circle(s)
#  t.end_fill()


def horline():
  t.fd(550)
  t.up()
  t.goto(0,0)
  t.pd()
  t.bk(510)
 
def verline():
  t.pu()
  t.goto(0,0)
  t.pd()
  t.sety(1000)
  t.pu()
  t.goto(0,0)
  t.pd()
  t.rt(90)
  t.fd(1000)
def co():
  t.goto(0,0)
  for I in range(10,200,20):
    t.circle(I)
  
def x_axis(length, step):
    for i in range(-length, length + 1, step):
        draw_line(i, 0, i, 0)
        t.write(str(i), align="center", move=False)
def draw_line(x1, y1, x2, y2):
    
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
def y_axis(length, step):
    for i in range(-length, length + 1, step):
        draw_line(0, i, 0, i)
        t.write(str(i), align="right", move=False)

#horline()
#verline()
#x_axis(500,100)
#y_axis(1000,100)
#co()
t.goto(-500,0)
t.fd(500)
t.rt(90)
t.fd(1000)
t.goto(0,0)
t.lt(90)
t.fd(500)
t.goto(0,0)
t.rt(270)
t.fd(1000)
t.goto(0,0)
x=(100)
for I in range(10,360,30):
  t.goto(x,I)
  t.circle(1)
  t.goto(0,0)
  t.pu()
  t.fd(math.tan(x))
  t.pd()
  t.lt(90)
  t.fd(40)
  x+=10
 



turtle.mainloop()
