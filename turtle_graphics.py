# import turtle
# import random
#
# # Set up the screen
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# directions = [0, 90, 180, 270]
# # Create the turtle
# walker = turtle.Turtle()
# walker.speed("fastest")  # Set the drawing speed
# walker.pensize(12)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# # Perform the random walk
# for _ in range(500):
#     walker.color(random.choice(colours))
#
#     step_length = random.randint(0, 100)
#     # Move the turtle forward
#     walker.forward(20)
#     # Move the turtle forward
#     walker.setheading(random.choice(directions))
#     # Turn the turtle by the random angle
#     # walker.right(angle)
#
# screen.exitonclick()
#
#
import turtle
import random
# Set up the screen
screen = turtle.Screen()
turtle.colormode(255)
screen.setup(width=600, height=600)

# Create the turtle
spiro_turtle = turtle.Turtle()
spiro_turtle.speed("fastest")  # Set the drawing speed

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
# Customize the spirograph parameters
R = 100  # Radius of the large circle
r = 30   # Radius of the small circle
d = 50   # Distance from the center of the small circle to the pen point

# Draw the spirograph
for _ in range(360):
    spiro_turtle.color(random_colour())  # Change color for each iteration
    spiro_turtle.circle(R)
    spiro_turtle.color(random_colour())
    spiro_turtle.circle(r)
    spiro_turtle.left(1)  # Rotate the turtle by 1 degree

# Hide the turtle
spiro_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
