import turtle
turtle.Screen().setup(200,300)
turtle.Screen().bgcolor("Pink")
pen=turtle.Turtle()
side=8
sidelength=100
angle=360/side
for i in range(side):
    pen.forward(sidelength)
    pen.right(angle)
turtle.done()