import time

# calculate how many seconds are in each unit of time
minute = 60
hour = 60 * minute
day = 24 * hour
year = 365 * day


def print_time(secs):
    """ A recursive function that prints the current time in hours, minutes, seconds
        secs = time in seconds since the epoch
        Uses floor divison to work out how many of the seconds are for years, days, etc. on each recursion
        Modulus is used to find the remaining number of seconds for future recursions after each floor division """
    y = int(secs // year)
    d = int(secs // day)
    h = int(secs // hour)
    m = int(secs // minute)
    if y != 0:
        print_time(secs % year)
    elif d != 0:
        print_time(secs % day)
    elif h != 0:
        print(str(h) + ':', end='') 
        print_time(secs % hour)
    elif m != 0:
        print(str(m) + ':', end='')
        s = int(secs % minute)
        if s < 10:
            print('0', end='')
        print(str(s))


def print_epoch_days(secs):
    print('It has been', int(secs // day), 'days since the epoch.')


print_time(time.time())
print_epoch_days(time.time())

