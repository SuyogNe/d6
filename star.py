import turtle
turtle.Screen().bgcolor("darkcyan")

a=turtle.Screen()
a.setup(700,700)

turtle.title("Square")

t=turtle.Turtle()
t.color("red")
t.fillcolor("white")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.right(150)
t.forward(50)

t.pendown()
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
turtle.done()