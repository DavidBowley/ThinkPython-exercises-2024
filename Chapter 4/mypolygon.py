import turtle
import math

bob = turtle.Turtle()
alice = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)   # all regular polygon external angles are 360 / number of sides

def circle(t, r):
    c = 2 * math.pi * r     # first work out the expected circumference based on the radius: 2*Pi*R
    sqrt = math.sqrt(c)     # square root gives us two numbers that can be used together to make the circumference
    polygon(t, int(sqrt), int(sqrt))    # length * n = circumference, so call polgyon function with the square root as length and number of sides
                                        # Note: math.sqrt gives a floating point which won't work for the circle function (needs a whole number for sides)
                                        # converting to integer fixes but we only get approximation of the radius to circumference formula due to this
                                        # rounding properly instead of using int (which just cuts everything after the decimal point) may be better

# calls the circle function, then draws the radius into the circle to confirm it's the expected approximate size
def confirm_radius(t, r):
    """explain the function
    it can be multi-line like so
    """
    circle(t, r)
    t.lt(90)
    t.fd(r)

# Read the circle and polygon functions above to understand the maths behind making an appoximate circle with a polygon
# This is a modified version of the same code that stops the circle after a certain number of degrees has passed
def arc(t, r, angle):
    c = 2 * math.pi * r         # The cirumference based on the given radius
    length = int(math.sqrt(c))  # The length of each side of the polgyon
    n = int(math.sqrt(c))       # The number of sides in the polygon (if it was allowed to fully complete the shape)
    x = int((angle / 360) * n)  # The actual number of sides we want in the arc...
                                # ...based on the given angle in degrees, as a percentage of the whole circle, multiplied by the total number of sides in the polygon
    for i in range(x):          # For loop creates 'x' number of sides, which is an approximation of the original angle given
        t.fd(length)
        t.lt(360 / n)

# a function I messed around with that creates many circles spiralling out with a for loop
def spirograph():
    for i in range(200):
        super_turtle = turtle.Turtle()
        circle(super_turtle, i)  





turtle.mainloop()
