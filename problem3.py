# Hikmet Tenis
# 08/02/2024
# This program draws a regular polygon based on user input.

import turtle

# Get user input
num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))
line_color = input("Enter the color of the line: ")
fill_color = input("Enter the fill color: ")

# Set up the turtle
polygon = turtle.Turtle()
polygon.color(line_color)
polygon.fillcolor(fill_color)

# Draw the polygon
polygon.begin_fill()
for _ in range(num_sides):
    polygon.forward(side_length)
    polygon.right(360 / num_sides)
polygon.end_fill()

# Complete the drawing
turtle.done()