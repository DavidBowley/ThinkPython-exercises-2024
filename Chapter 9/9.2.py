def has_no_e(s):
    if not 'e' in s:
        return True
    else:
        return False

def print_no_e_words():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)

def percentage_no_e_words():
    fin = open('words.txt')
    total = 0
    count = 0    
    for line in fin:
        total = total + 1
        word = line.strip()
        if has_no_e(word):
            count = count + 1
    return (count / total) * 100


#print_no_e_words()
print(percentage_no_e_words())