import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("#e654c0")
turtle_screen.title("Shrinking Squares")

turtle_instance=turtle.Turtle()
turtle_instance.color("white")

def shrinking_square(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5
shrinking_square(200)
shrinking_square(175)
shrinking_square(150)
shrinking_square(125)
shrinking_square(100)
shrinking_square(75)
shrinking_square(50)
shrinking_square(25)
shrinking_square(5)
turtle.done()

