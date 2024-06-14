def prep_string(s):
    """  Takes a string (s) and prepares it for use in the is_anagram function
         Returns a list of characters
    """
    s = s.replace(' ', '')      # removes all spaces from the string
    s = s.lower()               # converts to lower case
    s = sorted(s)               # sorts into an alphabetically ordered list of characters
    return s

def is_anagram(s1, s2):
    """ takes two strings (s1, s2) and checks if they are anagrams of each other """
    return prep_string(s1) == prep_string(s2)


test1 = 'a gentleman'
test2 = 'elegant man'
#print(is_anagram(test1, test2))

print(is_anagram(test1, test2))