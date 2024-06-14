import math
import copy
import turtle

class Point:
    """ Represents a point in 2-D space """

class Rectangle:
    """ Represents a rectangle in 2-D space
        attributes: width (float), height (float), corner (Point object) """

class Circle:
    """ Represents a circle in 2-D space
        attributes: center (Point object) and radius (float) 
    """

def distance_between_points(p1, p2):
    """ Returns the difference between the two Points (p1, p2)
        Expects a Point object as per the Point class
    """
    distance = math.sqrt(((p2.x - p1.x)**2 + (p2.y - p1.y)**2))
    return distance

def test_distance_between_points():
    point1 = Point()
    point2 = Point()

    point1.x = 3
    point1.y = 2

    point2.x = 7
    point2.y = 8

    print(distance_between_points(point1, point2))

def move_rectangle(rect, dx, dy):
    """ Takes a Rectangle object (rect) and moves its position by updating its corner Point object's x and y co-ordinates
    """
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_new(rect, dx, dy):
    """ Modified version of the above move_rectangle function that returns a new Rectangle instead of modifying the original
    """
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect

def create_test_box():
    box = Rectangle()
    box.width = 50
    box.height = 100
    box.corner = Point()
    box.corner.x = 75
    box.corner.y = 100

def point_in_circle(circ, p):
    """ Takes a Circle object and a Point object and returns True if the Point lies in or on the boundary of the circle
        circ = Circle object
        p = Point object
    """
    distance = distance_between_points(circ.center, p)
    # if the distance is less than the radius then the point is inside the circle
    # if it's the same as the radius then the point is on the edge of the circle
    # if it's greater than the radius then the point is outside the circle
    return distance <= circ.radius

def get_rect_points(rect):
    """ Calculates all the points of a given Rectangle object (rect)
        Returns a tuple of Point objects in the following order: bottom left, bottom right, top left, top right
    """
    bottom_left = copy.copy(rect.corner)
    bottom_right = copy.copy(rect.corner)
    bottom_right.x += rect.width
    top_left = copy.copy(rect.corner)
    top_left.y += rect.height
    top_right = copy.copy(rect.corner)
    top_right.x += rect.width
    top_right.y += rect.height
    return bottom_left, bottom_right, top_left, top_right  

def rect_in_circle(circ, rect):
    """ Takes a Circle object and a Rectangle object and returns True if the rectangle lies in or on the boundary of the circle
    """
    bottom_left, bottom_right, top_left, top_right = get_rect_points(rect)
    return point_in_circle(circ, bottom_left) and point_in_circle(circ, bottom_right) and point_in_circle(circ, top_left) and point_in_circle(circ, top_right)

def rect_circle_overlap(circ, rect):
    """ Takes a Circle object and a Rectangle object and returns True if the rectangle corners overlap the circle
    """
    # work out if any of the points of the rectangle are inside the circle, but NOT all the points
    bottom_left, bottom_right, top_left, top_right = get_rect_points(rect)
    if point_in_circle(circ, bottom_left) or point_in_circle(circ, bottom_right) or point_in_circle(circ, top_left) or point_in_circle(circ, top_right):
        if not rect_in_circle(circ, rect):
            return True
        else:
            return False
    else:
        return False

def draw_rect(t, rect):
    """ Takes a Turtle object (t) and a Rectangle object (rect) and uses the Turtle to draw the Rectangle
    """
    # Move the turtle to the rectangle's bottom-left corner
    t.pu()
    t.setpos(rect.corner.x, rect.corner.y)
    t.pd()
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)   # all regular polygon external angles are 360 / number of sides

def circle(t, r):
    c = 2 * math.pi * r     # first work out the expected circumference based on the radius: 2*Pi*R
    sqrt = math.sqrt(c)     # square root gives us two numbers that can be used together to make the circumference
    polygon(t, int(sqrt), int(sqrt)) 

def draw_circle(t, circ):
    """ Takes a Turtle object (t) and a Circle object (circ) and uses the Turtle to draw the Circle
    """
    circle(t, circ.radius)





my_circle = Circle()
my_circle.center = Point()
my_circle.center.x = 0
my_circle.center.y = 0
my_circle.radius = 50

my_rect = Rectangle()
my_rect.corner = Point()
my_rect.corner.x = -300
my_rect.corner.y = -250
my_rect.width = 500
my_rect.height = 500

bob = turtle.Turtle()
draw_circle(bob, my_circle)
turtle.mainloop()

# print(rect_in_circle(my_circle, my_rect))
# print(rect_circle_overlap(my_circle, my_rect))





