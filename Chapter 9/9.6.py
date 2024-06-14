def is_abecedarian(s):
    """ Takes a string (s) and returns True if the string's letters appear in alphabetical order
    """
    word = s.lower()        # make sure everything is lowercase for the ord() function to accurately work out relationship between letters
    last_letter = ''         

    for letter in word:
        current_letter = letter
        if current_letter < last_letter: 
            return False
        last_letter = current_letter
    return True

def is_abecedarian_while(s):
    """ Takes a string (s) and returns True if the string's letters appear in alphabetical order
    """
    word = s.lower()        # make sure everything is lowercase for the ord() function to accurately work out relationship between letters
    i = 0

    while i < len(word) - 1:
        if word[i] > word[i+1]:
            return False
        i = i + 1
    return True


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        count = count + 1

print(count)
