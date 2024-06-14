import polygon
import turtle

bob = turtle.Turtle()

def petal(t, r, angle):
    """ Creates a single petal using two arcs
    t = turtle object
    r = radius of the arc in degrees, larger number equals longer/larger petals
    angle = angle of the arc in degrees: smaller = thinner petals, larger = fatter petals
    NOTE: it's not really as simple as the above makes out, may need to play a bit to match the shape seen in the PDF
    """
    turn = (360.0 - angle * 2) / 2
    polygon.arc(t, r, angle)
    t.lt(turn)
    polygon.arc(t, r, angle)
    t.lt(turn)  # return turtle to orignal start orientation

def flower(t, n, size, intersect):
    """ Creates a single flower using multiple petals
    t = turtle object
    n = number of petals
    size = arbritary number that keeps each flower to a relative proportionate size, e.g. 20, 30, 40
    intersect = takes either a value of 1 (no intersect) or 2 (intersect)
    """
    turn = 360.0 / n    # work out how many degrees per petal 
    r = n * (size / intersect)      # Each flower will be an equal size as long as the radius is made from the number of sides multiplied by the same arbitrary number 
                                    # This is slightly different for the intersect variant, as the increased angle of the arc requires a similar decrease in the size multiplier for the radius to keep the same size   
    turtle.tracer(0, 0)
    for i in range(n):
        petal(t, r, turn*intersect) # If intersect is 1 then the angle of the petal is the same as each turtle turn to the next petal (therefore no intersection at all)
                                    # If intersect is 2 then the angle of the petal is twice the turtle turn and so causes an intersection between petals
        t.rt(turn)                  # turn right to start next petal
    turtle.update()


# first flower with 7 petals (no intersecting)
flower(bob, n=7, size=40, intersect=1)

# second flower with 10 petals (intersecting petals)
flower(bob, n=10, size=40, intersect=2)

# third flower with 20 petals (no intersecting)
flower(bob, n=20, size=40, intersect=1)

turtle.mainloop()