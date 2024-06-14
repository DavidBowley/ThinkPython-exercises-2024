import turtle
from polygon import polygon
import math



bob = turtle.Turtle()

def triangle_polygon(t, n, length):
    """ Draws an n-sided polygon with n number of equally sized isoceles triangles inside
    t = turtle object
    n = number of sides/triangles
    length = length of each polygon side in pixels
    """
    polygon(t, n, length)       # draws the external polygon shape
    
    radius = length / (2 * math.sin(math.radians(180 / n)) )        # gets the circumradius of the polygon (both sides a from the internal isoceles triangle)
    angle_a = (180 - 360 / n) / 2       # This is angle A from the isoceles triangle. Forumla is the polygon's interal angles divided by two.
    angle_b = 180 - (angle_a * 2)       # Formula to work out the vertex angle of the isoceles triangle if we know the other two angles

    # first triangle
    t.lt(angle_a)
    t.fd(radius)
    t.rt(180.0 - angle_b)
    t.fd(radius)

    # remaining triangles use the same action
    for i in range(n - 2):
        t.pu()
        t.lt(180)
        t.fd(radius)
        t.pd()
        t.rt(180.0 - angle_b)
        t.fd(radius)


def move_away(t):
    t.pu()
    t.fd(50)
    t.pd()


def all_the_triangles(t, n):
    for i in range(5, n + 1):
        triangle_polygon(t, i, 100)
        move_away(t)


triangle_polygon(bob, 12, 50)



turtle.mainloop()