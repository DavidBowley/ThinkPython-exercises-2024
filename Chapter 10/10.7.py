def has_duplicates(t):
    """ Takes a list (t) and returns True if there is any element that appears more than once
        Does not modify the original list
    """
    new_list = sorted(t)
    for i in range(len(new_list) - 1):              # we need to finish the loop one index less than the total length to avoid an index out of range error on the last comparison
        if new_list[i] == new_list[i+1]:
            return True
    return False


def has_duplicates_2(t):
    """ Takes a list (t) and returns True if there is any element that appears more than once
        Does not modify the original list
        Slightly different version that creates a new list that consists of all the items except the current item,
        then checks if the current item is in the remainder (and therefore a duplicate)
    """
    for i in range(len(t)):
        new_list = t[:]         # create a copy of the list
        del new_list[i]         # remove the current list item from the new list
        if t[i] in new_list:    # if the current list item (from original list) is in the new list, then the same entry was in more than once
            return True
    return False




test = [1, 2, 3, 4, 5, 1]
print(has_duplicates_2(test))