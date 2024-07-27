# we have to create a new program that will work such that it will go forward on w and backwards on s and anticlockwise on a and clockwise on d
from turtle import Turtle,Screen
turtle_1 = Turtle()

def forward():

    turtle_1.forward(100)
def backward():
    turtle_1.setheading(180)
    turtle_1.backward(-100)

def right():
    new_heading = turtle_1.heading()-10
    turtle_1.setheading(new_heading)
def left():
    new_heading = turtle_1.heading()+10
    turtle_1.setheading(new_heading)
def clear():
    turtle_1.clear()
    turtle_1.penup()
    turtle_1.home()
    turtle_1.pendown()
    turtle_1.setheading(0)
screen = Screen()
screen.listen()#using this method the turtle starts to take inputs into consideration
''''the onkey function takes only non arguments function'''
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(right,"r")
screen.onkey(left,"l")
screen.onkey(clear,"c")

screen.exitonclick()