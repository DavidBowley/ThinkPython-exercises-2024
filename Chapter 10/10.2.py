def cumsum(t):
    new_list = []
    for i in range(len(t)):
        new_list.append(sum(t[:i+1]))
    return new_list


test = [1, 2, 3, 4, 5]
print(cumsum(test))