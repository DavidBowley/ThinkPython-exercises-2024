def practice_center(s):
    index = 0
    while index < 10:
        line = ''
        for i in range(index):
            if i == index - 1:
                line = line + s
            else:
                line = line + s + ' '
        print(line.center(100))
        index = index + 1

#my_string = 'testing 123 here we go brap brap brap'
#print(my_string.replace('brap', 'no braps today'))


practice_center("test test test")