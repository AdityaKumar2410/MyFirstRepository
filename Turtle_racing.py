from turtle import Screen,Turtle
import random

screen = Screen()
screen.setup(width=500,height=400)
user_inp = screen.textinput(title="Enter your choice of the turtle color that you think will win!!",prompt="Enter the color!!!")
class TurtleColor:
    def __init__(self,color,x,y):
        self.color = color
        self.turtle = Turtle()

        self.turtle.shape("turtle")
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.goto(x=x,y=y)
        self.turtle.speed("slowest")

    def random_walk(self):
        # while True:
            walk = random.randint(0,10)
            self.turtle.penup()
            self.turtle.forward(walk)
    def win(self):
        if self.turtle.xcor() > 230:
            return False



list_of_turtles = []


colours = ["red", "green", "blue", "yellow", "purple", "orange"]
if user_inp not in colours:
    print("You lose!!Ennter a valid colour!")
    screen.bye()
else:
    print("If you want to exit click on the screen!!")
    for colour in range(0,6):
        colours[colour] = TurtleColor(colours[colour],-235,-100+colour*50)
        list_of_turtles.append(colours[colour])
    a = True
    while a:
        for i in list_of_turtles:
            i.random_walk()
            if i.win() == False:
                a=False
                winner = i.color
    print(winner)
    if winner != user_inp:
        print("You lose!!")
        print(f"You chose {user_inp} but the winner was {winner}!!!!!!!!!!!!!!!!")
    else:
        print("You win!!")
        print(f"The winner was {user_inp}")

    screen.exitonclick()