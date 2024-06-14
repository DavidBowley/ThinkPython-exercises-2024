def has_duplicates(t):
    """ Takes a list (t) and returns True if there is any element that appears more than once
        Does not modify the original list
        This is an improved version of exercise 10.7 that uses a dictonary instead of potentially traversing the whole list with a for loop
    """

    # Create the dictonary to store any previously seen list values
    known = {}
    # Create a new sorted list
    sorted_list = sorted(t)
    # Traverse the list and add any values seen to the dictionary (a memo)
    # If the previously seen value is seen in a later iteration then we have found a duplicate
    for list_item in sorted_list:
        if list_item in known:
            return True
        known[list_item] = 1
    return False


test = [1, 2, 3, 4, 5, 1]
print(has_duplicates(test))