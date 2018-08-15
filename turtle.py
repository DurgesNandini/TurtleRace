from tkinter import*
from turtle import *
from random import randint

speed(15)
penup()
goto(-200,200)
step=0
for step in range(11):
    write(step,align='center')
    right(90)
    forward(10)
    pendown()
    forward(130)
    penup()
    backward(140)
    left(90)
    forward(25)
t1=Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-220,170)
t1.pendown()
t2=Turtle()
t2.color('yellow')
t2.shape('turtle')
t2.penup()
t2.goto(-220,140)
t2.pendown()
t3=Turtle()
t3.color('blue')
t3.shape('turtle')
t3.penup()
t3.goto(-220,110)
t3.pendown()
t4=Turtle()
t4.color('green')
t4.shape('turtle')
t4.penup()
t4.goto(-220,80)
t4.pendown()
a=('winner')
goto(0,-11)
write(a)
addt1=0
addt2=0
addt3=0
addt4=0
for turn in range(180):
    a1=randint(1,5)
    a2=randint(1,5)
    a3=randint(1,5)
    a4=randint(1,5)
    t1.forward(a1)
    t2.forward(a2)
    t3.forward(a3)
    t4.forward(a4)
    addt1+=a1
    addt2+=a2
    addt3+=a3
    addt4+=a4

    if addt1>=300:
        t1.goto(0,10)
        break
    if addt2>=300:
        t1.goto(0,10)
        break
    if addt3>=300:
        t3.goto(0,10)
        break
    if addt4>=300:
        t4.goto(0,10)
        break



