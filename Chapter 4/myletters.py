import polygon

m = 2   # modifer for width to height ratio in each character
        # 2 = 1:2 ratio from width to height

def guideline(t, s):
    """ draws a guideline around the invisible rectangular area for the letter to help with designing the letters
    will be removed one the letter design is finished
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / 2      # used for font width, 1:2 ratio with the height
    t.lt(90)
    for i in range(2):
        t.fd(h)
        t.rt(90)
        t.fd(w)
        t.rt(90)
    t.rt(90)


def skip(t, s):
    """ Move to the right ready for the next character
    t = turtle object
    s = size (this is the overall size in typewriter.py divided by 2)
    """
    t.pu()
    t.fd(s)
    t.pd()

    # write code to skip the letter

def draw_a(t, s):
    """ Draws a letter A
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h)
    t.rt(90)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.pu()
    t.rt(180)
    t.fd(h / 3)
    t.lt(90)
    t.pd()
    t.fd(w)
    t.pu()
    t.rt(180)
    t.fd(w)
    t.rt(90)
    t.fd(h / 3)
    t.lt(90)

def draw_b(t, s):
    """ Draws a letter B
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h)
    t.pu()
    t.rt(180)
    t.fd(h)
    t.lt(90)
    t.pd()
    t.fd(w * 0.666)
    polygon.arc(t, h / 4, 180)
    t.fd(w * 0.666)
    t.pu()
    t.rt(180)
    t.fd(w * 0.666)
    t.pd()
    polygon.arc(t, h / 4, 180)
    t.fd(w * 0.666)
    t.pu()
    t.rt(180)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.lt(90)

def draw_c(t, s):
    """ Draws a letter C
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.pu()
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.pd()
    polygon.arc(t, h / 2, 180)

def draw_d(t, s):
    """ Draws a letter D
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h)
    t.pu()
    t.rt(180)
    t.fd(h)
    t.lt(90)
    t.pd()
    polygon.arc(t, h / 2, 180)
    t.pu()
    t.rt(180)
    t.fd(w)
    t.rt(90)
    t.fd(h)
    t.lt(90)

def draw_e(t, s):
    """ Draws a letter E
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h)
    t.rt(90)
    t.fd(w)
    t.pu()
    t.rt(180)
    t.fd(w)
    t.lt(90)
    t.fd(h / 2)
    t.lt(90)
    t.pd()
    t.fd(w)
    t.pu()
    t.rt(180)
    t.fd(w)
    t.lt(90)
    t.fd(h / 2)
    t.lt(90)
    t.pd()
    t.fd(w)

def draw_f(t, s):
    """ Draws a letter F
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h)
    t.rt(90)
    t.fd(w)
    t.pu()
    t.rt(180)
    t.fd(w)
    t.lt(90)
    t.fd(h / 2)
    t.lt(90)
    t.pd()
    t.fd(w)
    t.pu()
    t.rt(90)
    t.fd(h /2)
    t.lt(90)

def draw_g(t, s):
    """ Draws a letter G
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    draw_c(t, s)
    t.lt(90)
    t.fd(h / 3)
    t.lt(90)
    t.fd(w / 3)
    t.pu()
    t.rt(180)
    t.fd(w / 3)
    t.rt(90)
    t.fd(h / 3)
    t.lt(90)

def draw_h(t, s):
    """ Draws a letter H
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h)
    t.pu()
    t.rt(180)
    t.fd(h /2)
    t.lt(90)
    t.pd()
    t.fd(w)
    t.pu()
    t.lt(90)
    t.fd(h / 2)
    t.rt(180)
    t.pd()
    t.fd(h)
    t.lt(90)

def draw_i(t, s):
    """ Draws a letter I
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.pu()
    t.fd(w / 2)
    t.lt(90)
    t.pd()
    t.fd(h)
    t.pu()
    t.rt(90)
    t.fd(w / 2)
    t.rt(90)
    t.fd(h)
    t.lt(90)

def draw_j(t, s):
    """ Draws a letter J
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.pu()
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.rt(180)
    t.pd()
    t.fd(h * 0.75)
    t.pu()
    t.rt(180)
    polygon.arc(t, w / 2, 180)
    t.pd()
    polygon.arc(t, w / 2, 180)
    t.pu()
    t.rt(180)
    t.fd(h * 0.25)
    t.lt(90)

def draw_k(t, s):
    """ Draws a letter K
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.lt(90)
    t.fd(h / 2)
    x = t.pos()
    t.fd(h / 2)
    t.pu()
    t.rt(90)
    t.fd(w)
    y = t.pos()
    t.rt(90)
    t.fd(h)
    t.pd()
    t.goto(x)
    t.goto(y)
    t.pu()    
    t.fd(h)
    t.lt(90)

def draw_l(t, s):
    """ Draws a letter L
    t = turtle object
    s = size
    """
    h = s          # used for font height
    w = s / m      # used for font width, see global variable m for modifier
    t.pu()
    t.lt(90)
    t.fd(h)
    t.rt(180)
    t.pd()
    t.fd(h)
    t.lt(90)
    t.fd(w)
    