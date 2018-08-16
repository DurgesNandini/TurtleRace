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
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
t1=Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(-220,170)
t1.pendown()
for turn in range(10):
    t1.right(36)
t2=Turtle()
t2.color('yellow')
t2.shape('turtle')
t2.penup()
t2.goto(-220,140)
t2.pendown()
for turn in range(72):
    t2.left(5)
t3=Turtle()
t3.color('blue')
t3.shape('turtle')
t3.penup()
t3.goto(-220,110)
t3.pendown()
for turn in range(60):
    t3.right(6)
t4=Turtle()
t4.color('green')
t4.shape('turtle')
t4.penup()
t4.goto(-220,80)
t4.pendown()
for turn in range(30):
    t4.left(12)
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
    if addt1>=230:
        t1.goto(0,10)
        break
    if addt2>=230:
        t1.goto(0,10)
        break
    if addt3>=230:
        t3.goto(0,10)
        break
    if addt4>=230:
        t4.goto(0,10)
        break
   



