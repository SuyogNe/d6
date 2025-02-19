import turtle


t=turtle.Turtle()
s=turtle.Screen()

colors=['red', 'purple', 'blue', 'green', 'orange', 'yellow']

s.bgcolor('black')
t.speed("fastest")

t.hideturtle()

while True:
    for i in range(200):
        t.pencolor(colors[i%len(colors)])
        t.width(i/100+1)
        t.forward(i)
        t.left(59)
    t.right(239)

    for i in range (200,0,-1):
        t.pencolor("black")
        t.width(i/100+7)
        t.forward(i)
        t.right(59)