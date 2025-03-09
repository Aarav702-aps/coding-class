import turtle #importing libary

paper = turtle.Screen() # make the paper on the screen
paper.bgcolor("blue") # set the backgrond color
paper.setup(300,400) # width = 300, height = 400
paper.title("polygon")

pen = turtle.Turtle() # make the pen

num_sides = 6 #number of hexagon's sides
side_length = 70

angle = 360 / num_sides

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angle)

turtle.done()