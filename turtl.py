import turtle
turtle.Screen().bgcolor("darkcyan")

a=turtle.Screen()
a.setup(700,700)

turtle.title("Square")

t=turtle.Turtle()
t.color("red")
t.fillcolor("white")

for i in range(8):
    t.forward(100)
    t.left(45)
    i=i+1
turtle.done()