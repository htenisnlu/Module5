# Hikmet Tenis
# 08/02/2024
# This program draws a creative picture using turtle graphics.

import turtle

# Set up the turtle
artist = turtle.Turtle()

# Draw a creative shape
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle.bgcolor('black')

for x in range(360):
    artist.pencolor(colors[x % 6])
    artist.width(x // 100 + 1)
    artist.forward(x)
    artist.left(59)

# Complete the drawing
turtle.done()