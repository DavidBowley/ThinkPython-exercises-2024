import sys
sys.path.append('../Chapter 12')
from twelve_ex2 import find_anagrams_dict
import shelve

def store_anagrams(anagram_set):
    """ Stores the anagram_set in a shelf
        anagram_set = dictionary as exported from the find_anagrams_dict function
    """
    anagram_shelf = shelve.open('shelve_testing')
    anagram_shelf['anagram_set'] = anagram_set
    anagram_shelf.close()

def read_anagrams(word):
    """ Looks up a word in the anagram_set currently stored in a shelf
        word = string we want to search for
    """
    anagram_shelf = shelve.open('shelve_testing')
    anagram_set = anagram_shelf['anagram_set']
    search = tuple(sorted(word))
    if search in anagram_set:
        return anagram_set[search]
    else:
        return None


# anagram_dict = find_anagrams_dict('words.txt')
print(read_anagrams('spot'))



