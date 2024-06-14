import turtle

bob = turtle.Turtle()

def koch(t, x, angle, z):
    """ Draws a Koch curve of length X
    t = turtle object
    x = length
    """
    if x < z:
        t.fd(x)
        return
    koch(t, x / z, angle, z)
    t.lt(angle)
    koch(t, x / z, angle, z)
    t.rt(angle * 2)
    koch(t, x / z, angle, z)
    t.lt(angle)
    koch(t, x / z, angle, z)

def koch2(t, x):
    """ Draws a Koch curve of length X
    t = turtle object
    x = length
    """
    if x < 3:
        t.fd(x)
        return
    koch2(t, x / 3)
    t.lt(60)
    koch2(t, x / 3)
    t.rt(120)
    koch2(t, x / 3)
    t.lt(60)
    koch2(t, x / 3)

def snowflake(t):
    turtle.tracer(0,0)
    for i in range(3):
        koch(t, 100)
        t.rt(120)
    turtle.update()

def new_snowflake(t):
    turtle.tracer(0,0)
    for i in range(4):
        koch(t, 100, 60, 4)
        t.rt(90)
    turtle.update()

def snowflake2(t):
    turtle.tracer(0,0)
    for i in range(4):
        koch2(bob, 1000)
        t.rt(90)
    
    turtle.update()

snowflake2(bob)


turtle.mainloop()