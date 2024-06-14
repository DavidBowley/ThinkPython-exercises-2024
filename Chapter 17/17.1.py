# Note: this was a copy of 17.py before the changes requested in exercise 17.1 were made

import copy

class Time:
    """ Represents the time of day.
    attributes: hour, minute, second
    Note that any unit of time smaller than a second is rounded to the nearest second
    """

    def __init__(self, hour=0, minute=0, second=0):
        minutes = hour * 60 + minute
        seconds = minutes * 60  + second
        self.second = seconds

    def __str__(self):
        # temp variables as need to use int() on minutes and seconds after divmod()
        m, s = divmod(self.second, 60)
        # int(s) truncates to just seconds and ignores 100th seconds and further
        # Note: choosing to truncate rather than round as this seems to be the most common way for races if we are at the desired precision level
        # int(m) converts from a float (depending on the caller sometimes this is needed)
        m, output_second = int(m), int(s)
        output_hour, output_minute = divmod(m, 60)
        return f'{output_hour:02d}' + ':' + f'{output_minute:02d}' + ':' + f'{output_second:02d}'

    def __lt__(self, other):
        return self.second < other.second

    def __eq__(self, other):
        return self.second == other.second

    def increment(self, seconds):
        return int_to_time(seconds + self.second)

    def is_after(self, other):
        """ Takes a Time object (self) and checks to see if it appears chornologically after a 2nd Time object (other)
        """
        return self.second > other.second

    def mul_time(self, n):
        """ Takes a Time object (self) and multiplies it by the number (n) """
        return int_to_time(self.second * n)

    def time_per_mile(self, distance):
        """ Works out the time per mile for a given race finishing time and distance of the race
            self = a Time object
            distance = an integer in miles
            Returns a Time object
        """
        return int_to_time(self.second / distance)

def int_to_time(seconds):
    time = Time(second=seconds)
    return time


start = Time(6)
end = Time(6)
same_start = start

print(start == end)