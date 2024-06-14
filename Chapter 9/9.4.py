def uses_only(s, l):
    """ takes a string (s) and returns True if the word is only comprised of the letters in the list (l)
    """
    for letter in s:
        if letter not in l:
            return False
    return True

def uses_all(s, l):
    """ takes a string (s) and returns true if the required letters (l) are used at least once
    """
    for letter in l:
        if letter not in s:
            return False
    return True


#fin = open('words.txt')
#
#for line in fin:
#    word = line.strip()
#    if uses_only(word, 'acefhlo'):
#        print(word)


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy'):
        count = count + 1

print(count)

