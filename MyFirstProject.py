import turtle
t = turtle.Pen()
turtle.bgcolor('black')
sides = 6
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
for x in range(360):
    t.pencolor(colors[x % sides])
    t.circle(x)
    t.left(360/sides + 1)
    t.width(x*sides/200)