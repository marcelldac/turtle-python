from turtle import *

speed(100)
bgcolor('black')
pensize(0.1)

colors= ['red', 'green', 'blue', 'orange', 'cyan', 'red']

for i in range(6):
    for color0 in colors:
        color(color0)
        circle(150)
        left(10)
done()