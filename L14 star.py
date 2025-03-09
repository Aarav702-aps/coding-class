import turtle #importing libary

paper = turtle.Screen() # make the paper on the screen
paper.bgcolor("blue") # set the backgrond color
paper.setup(500,500) # width = 500, height = 500
paper.title("star of david")

pen = turtle.Turtle() # make a pen

# first triangle for star
pen.pendown()
pen.forward(100) # draw base

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

# change the postion of the pen
pen.penup()
pen.right(150)
pen.forward(50)

 # sencond triangle for star
pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

turtle.done()