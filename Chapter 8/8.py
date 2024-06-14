def reverse_letters(s):
    i = len(s) - 1
    while i >= 0:
        print(s[i])
        i = i - 1

def ducks():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if letter == 'Q' or letter == 'O':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)


def find(word, letter, i):
    index = i
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word, letter):
    index = 0
    count = 0
    while True:
        found = find(word, letter, index)
        if found == -1:
            return count
        elif found >= 0:
            count = count + 1
            index = found + 1

print(count('bbbbbcccccrrrrr', 'c'))