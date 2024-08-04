import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Spiral Helix")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")
turtle_colors=["red","pink","blue","green","orange","yellow","grey","black"]

for i in range(10):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)

turtle.done()