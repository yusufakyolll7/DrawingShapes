import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("#4BCBCF")
drawing_board.title("Python Turtle")
turtle_instance=turtle.Turtle()
num_sides = 5
angle = 360.0 / num_sides * 2
side_length = 300
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)
turtle.done()
'''for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(200)
turtle.done()'''

'''turtle_instance=turtle.Turtle()
turtle_instance.left(60)
turtle_instance.forward(200)
turtle_instance.right(120)
turtle_instance.forward(200)
turtle_instance.right(150)
turtle_instance.forward(250)
turtle_instance.right(150)
turtle_instance.forward(250)
turtle_instance.right(150)
turtle_instance.forward(275)
turtle.done()'''