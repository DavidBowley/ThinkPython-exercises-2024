#  Note: some partial changes were made based on information provided in chapter 17. However, the full changes are in the Chapter 17 folder

import copy

class Point:
    """ Represents a point in 2-D space """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'X: ' + str(self.x) + '\nY: ' + str(self.y)

    def __add__(self, other):
        output_point = Point()
        if isinstance(other, Point):
            output_point.x = self.x + other.x
            output_point.y = self.y + other.y
        elif isinstance(other, tuple):
            output_point.x = self.x + other[0]
            output_point.y = self.y + other[1]
        else:
            raise TypeError('Point addition requires either Point or Tuple objects')
        return output_point

    def __radd__(self, other):
        return self.__add__(other)

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}' + ':' + f'{self.minute:02d}' + ':' + f'{self.second:02d}'

    def print_time(self):
        """ Takes a Time object (t) and prints it in the format hour:minute:second
        """
        print(f'{self.hour:02d}' + ':' + f'{self.minute:02d}' + ':' + f'{self.second:02d}')

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60  + self.second
        return seconds

    def increment(self, seconds):
        """ Rewrite using time_to_int and int_to_time functions
        """
        return int_to_time(seconds + Time.time_to_int(self))

    def is_after(self, other):
        """ Takes a Time object (self) and checks to see if it appears chornologically after a 2nd Time object (other)
        """
        return format_time(self) > format_time(other)

def format_time(t):
    """ Takes a Time object (t) and formats it into a 6-digit number for comparisons
    """
    return f'{t.hour:02d}' + f'{t.minute:02d}' + f'{t.second:02d}'

def is_after(t1, t2):
    """ Takes a Time object (t1) and checks to see if it appears chornologically after a 2nd Time object (t2)
    """
    return format_time(t1) > format_time(t2)

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        # total number of whole minutes
        m = seconds // 60
        time.second -= (60 * m)
        time.minute += m

    if time.minute >= 60:
        # total number of whole hours
        h = time.minute // 60
        time.minute -= (60 * h)
        time.hour += h

def increment_pure(t, seconds):
    time = copy.copy(t)

    time.second += seconds

    if time.second >= 60:
        # total number of whole minutes
        m = seconds // 60
        time.second -= (60 * m)
        time.minute += m

    if time.minute >= 60:
        # total number of whole hours
        h = time.minute // 60
        time.minute -= (60 * h)
        time.hour += h

    return time

def increment_rewrite(t, seconds):
    """ Rewrite using time_to_int and int_to_time functions
    """
    return int_to_time(seconds + time_to_int(t))
    

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60  + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(time, n):
    """ Takes a Time object (time) and multiplies it by the number (n) """
    seconds = time_to_int(time)
    return int_to_time(seconds * n)

def time_per_mile(time, distance):
    """ Works out the time per mile for a given race finishing time and distance of the race
        time = a Time object
        distance = an integer in miles
        Returns a Time object
    """
    print(time_to_int(time) / distance)
    # return int_to_time(time_to_int(time) / distance)


start = Time(6)


# print(is_after(time, time2))
# pure_time = increment_pure(time, 21600)
# print_time(pure_time)
# print(time_to_int(time))
# print_time(increment_rewrite(time, 180))
# print_time(mul_time(time, 3))
# time_per_mile(time2, 26)

my_point = Point(100, 100)
second_point = Point(50, 50)
third_point = Point(10, 10)

print(123 + my_point)
