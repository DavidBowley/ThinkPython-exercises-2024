def avoids(s, l):
    """ takes a string (s) and returns True if it does not contain the forbidden letters (l)
    """
    for letter in s:
        if letter in l:
            return False
    return True


forbidden = input("Type in your forbidden characters and we will check the list for any words that don't include these characters: ")
forbidden = forbidden.lower()

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if avoids(word, forbidden):
        count = count + 1

print(count)

