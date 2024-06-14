import math
import turtle

bob = turtle.Turtle()

for i in range(400):
    t = i / 20 * math.pi
    x = (1 + 5 * t) * math.cos(t)
    y = (1 + 5 * t) * math.sin(t)
    bob.goto(x, y)


turtle.mainloop()