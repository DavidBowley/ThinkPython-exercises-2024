"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import sys
import string
import random

class Markov():

    def __init__(self, filename, order=2):
        self.suffix_map = {}
        self.prefix = ()
        self.filename = filename
        self.order = order
        self.word = ''
        self.process_file()

    def process_file(self):
        """Reads a file and performs Markov analysis.

        filename: string
        order: integer number of words in the prefix

        Returns: map from prefix to list of possible suffixes.
        """
        fp = open(self.filename, encoding='utf8')
        skip_gutenberg_header(fp)

        for line in fp:
            for word in line.rstrip().split():
                self.word = word
                self.process_word()

    def process_word(self):
        """Processes each word.

        word: string
        order: integer

        During the first few iterations, all we do is store up the words; 
        after that we start adding entries to the dictionary.
        """
        if len(self.prefix) < self.order:
            self.prefix += (self.word,)
            return

        try:
            self.suffix_map[self.prefix].append(self.word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffix_map[self.prefix] = [self.word]

        self.prefix = shift(self.prefix, self.word)

    def random_text(self, n=100):
        """Generates random wordsfrom the analyzed text.

        Starts with a random prefix from the dictionary.

        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        start = random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                self.random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = shift(start, word)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('***'):
            break

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


if __name__ == '__main__':
    time_machine = Markov(filename='the_time_machine.txt')
    time_machine.random_text()
    print('\n')
    p_and_p = Markov(filename='pride_and_prejudice.txt')#
    p_and_p.random_text()
