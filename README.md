
import turtle
import colorsys
import random
import math
t=turtle.Turtle()
s=turtle.Screen()
t.pensize(0.6)
t.speed(100)
s.title('range')
c=['red','black','brown','#08FF32']
#s.bgcolor('brown')
t.pencolor('red')
def square(): #square
	for i in range(4):
		t.fd(100)
		t.lt(90)
def neon():    #neon gemotry web
		for i in range(300):
			t.pencolor(c[i%len(c)])
			t.fd(i*1.5)
			t.lt(91)
def star():# star shape
		for i in range (200):
			t.pencolor(c[i%4])
			t.fd(i*2)
			t.rt(144)
			t.fd(i)
			t.lt(36)
		
def fun(): #fun circle
	for i in range(200):
		t.circle(i*2)
		t.rt(180)


def fa():# change color with circle
	for i in range(230):
		for j in range(3):
			j=colorsys.hsv_to_rgb(i/18,0.8,0.9)
			m=colorsys.hsv_to_rgb(i/8,0.4,0.7)
			s.bgcolor(j)
			t.pencolor(m)
			t.circle(50)
			t.rt(30)



def cm():     #change shape acc to angle
	r=random.randint(1,500)
	for i in range(500):
		
		t.fd(i)
		t.penup()
		t.rt(r)
		t.pd()


def r():    #run diffrential equation 
	s.bgcolor('black')
	fx=random.randint(1,10)
	fy=random.randint(1,10)
	scale=200
	turtle.tracer(3,0)
	t.pu()
	for i in range(629):
		time=i/100
		x=scale*math.sin(fx*time)
		y=scale*math.sin(fy*time)
		c=colorsys.hsv_to_rgb(i/628,1,1)
		t.color(c)
		t.goto(x,y)
		if i==0:
			t.pd()
	
	







r()
turtle.done()
