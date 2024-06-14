import copy

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    Note that any unit of time smaller than a second is rounded to the nearest second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}' + ':' + f'{self.minute:02d}' + ':' + f'{self.second:02d}'

    def print_time(self):
        """ Takes a Time object (self) and prints it in the format hour:minute:second
        """
        print(f'{self.hour:02d}' + ':' + f'{self.minute:02d}' + ':' + f'{self.second:02d}')

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60  + self.second
        return seconds

    def increment(self, seconds):
        """ Rewrite using time_to_int and int_to_time functions
        """
        return int_to_time(seconds + self.time_to_int())

    def is_after(self, other):
        """ Takes a Time object (self) and checks to see if it appears chornologically after a 2nd Time object (other)
        """
        return self.time_to_int() > other.time_to_int()

    def mul_time(self, n):
        """ Takes a Time object (self) and multiplies it by the number (n) """
        seconds = self.time_to_int()
        return int_to_time(seconds * n)

    def time_per_mile(self, distance):
        """ Works out the time per mile for a given race finishing time and distance of the race
            self = a Time object
            distance = an integer in miles
            Returns a Time object
        """
        return int_to_time(self.time_to_int() / distance)

def int_to_time(seconds):
    time = Time()
    # temp variables as need to use int() on minutes and seconds after divmod()
    m, s = divmod(seconds, 60)
    # int(s) truncates to just seconds and ignores 100th seconds and further
    # Note: choosing to truncate rather than round as this seems to be the most common way for races if we are at the desired precision level
    # int(m) converts from a float (depending on the caller sometimes this is needed)
    m, time.second = int(m), int(s)
    time.hour, time.minute = divmod(m, 60)
    return time


race = Time(2,30)

print(race.time_per_mile(26))