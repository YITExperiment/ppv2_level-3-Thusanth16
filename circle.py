import turtle

from itertools import cycle
colors = cycle(['maroon', 'blue', 'pink', 'gold', 'yellow', 'navy'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(blue))
    turtle.pencolor(next(red))
    turtle.circle(size)
    turtle.right(cycle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(30,0,1
