def is_double_letter_x3(s):
    i = 0
    while i < len(s) - 5:
        if s[i] == s[i+1] and s[i+2] == s[i+3] and s[i+4] == s[i+5]:
            return True
        i = i + 1
    return False

fin = open('words.txt')

for line in fin:
    word = line.strip()
    if is_double_letter_x3(word):
        print(word)
