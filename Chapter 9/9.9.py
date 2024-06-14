def check_reversed(n):
    if n < 10:                      # add leading zeros from ages 1 to 9
        age = str(n).zfill(2)
    else:
        age = str(n)
    
    reversed_age = age[::-1]

    if int(reversed_age) > int(age) and int(reversed_age) <= 120:
        return int(reversed_age)
    else:
        return -1

def same_age_gap(n, age_gap):
    
    while n <= 120:
        reversed = check_reversed(n)
        if reversed != -1:
            gap = reversed - n
            if gap == age_gap:
                print(n, reversed, gap)
        n = n + 1

i = 1

finished_ages = ''

while i <= 120:
    reversed = check_reversed(i)
    
    if reversed != -1:
        age_gap = reversed - i
        print(i, reversed, age_gap)
        
        if str(age_gap) not in finished_ages:
            same_age_gap(i + 1, age_gap)
            finished_ages = finished_ages + str(age_gap) + ','
            
        #print(finished_ages)


        # next_age = i + age_gap
        # print(i, reversed, age_gap)

    i = i + 1

print(finished_ages)