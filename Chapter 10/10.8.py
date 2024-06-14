import random

def has_duplicates(t):
    """ Takes a list (t) and returns True if there is any element that appears more than once
        Does not modify the original list
    """
    new_list = sorted(t)
    for i in range(len(new_list) - 1):              # we need to finish the loop one index less than the total length to avoid an index out of range error on the last comparison
        if new_list[i] == new_list[i+1]:
            return True
    return False

def generate_birthdays(n):
    """ Takes an integer (n) to generate n number of random birthdays
        Returns a nested list of birthdays: each inner list is in format [day, month]
    """
    # initialise the list
    birthdays = []

    # generate n number of birthdays and append to the list
    for i in range(n):
        # generate a random month from 1 - 12
        month = random.randint(1, 12)
        # generate a random day of the month (depending on which month it is)
        # 28 days possible for February (note that while 29th February is always a valid possible birthday, the Birthday Problem usually discounts these)
        if month == 2:
            day = random.randint(1, 28)
        # 30 days possible for April, June, September, and November
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day = random.randint(1, 30)
        # 31 days possible for all other months
        else:
            day = random.randint(1, 31)
        # add day and month to a list and return
        birthday = [day, month]
        birthdays.append(birthday)
    return birthdays

def birthday_probability(n, interval):
    """ runs the Birthday Problem scenario over and over, constantly updating the percentage of times a matched birthday was found
        n = number of times to run the problemm
        interval = how often to feedback the current percentage (testing showed every 10,000 iterations is a couple of seconds)
        should give an approximate calculation of the probability, with greater accuracy the more iterations are run
    """
    true_result = 0
    false_result = 0
    timer = interval - 1
    for i in range(n):

        if has_duplicates(generate_birthdays(23)):
            true_result += 1
        else:
            false_result += 1
        total = true_result + false_result
        percentage = (true_result / total) * 100
        percentage = round(percentage, 4)

        # print the stats every [interval] iterations
        if i == timer:
            print('Number of iterations: ', f"{total:,}")
            print('Estimated probability: ', percentage, '\n')
            timer += interval
    
    return percentage


print(birthday_probability(n=100000000, interval=10000))