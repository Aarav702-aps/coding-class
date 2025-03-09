import turtle #importing libary

paper = turtle.Screen() # make the paper on the screen
paper.bgcolor("blue") # set the backgrond color
paper.title("turtle")

pen = turtle.Turtle() # make the pen
size = 0

while True:
    for i in range(4):
        pen.forward(size + 1)
        pen.left(90)
        size = size - 5

    size = size + 1