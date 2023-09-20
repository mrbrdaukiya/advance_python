from turtle import *
import turtle
import colorsys

speed(0)
bgcolor("black")
h = 10
for i in range(16):
    for j in range(15):
        c = colorsys.hls_to_rgb(h, 1, 1)
        color(c)
        h+= 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt = (180)
    circle(40, 24)
turtle.done()
