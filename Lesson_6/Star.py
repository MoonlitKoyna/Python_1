import turtle

turtle.Screen().bgcolor("Purple")
board= turtle.Turtle()

#1st Triangle
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#2nd Triangle
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)


turtle.done()