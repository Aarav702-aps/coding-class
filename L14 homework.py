import turtle

paper = turtle.Screen()
paper.bgcolor("white")
paper.setup(300,400)
paper.title("square")

pen = turtle.Turtle()

num_sides = 4
side_length = 70

angle = 360 /num_sides

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angle)

turtle.done()