def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    """ Checks if a word is a palindrome by recursively checking if each middle (minus first and last letters) is also a palindrome
    """
    if first(s) == last(s) and len(middle(s)) > 1 and is_palindrome(middle(s)):     # If the first and last letters are the same, the middle letters still exist, and the middle is a palindrome also
        return True
    elif first(s) == last(s) and len(middle(s)) <= 1:                               # If the first and last letters are the same, but the middle letters no longer exist...
        return True                                                                 # ... then this is the end of the recursion and it must be a palindrome
    else:                                                                           # Any other condition would not be a palindrome
        return False


print(is_palindrome('ABBAABBAABBAABBAABBA'))
