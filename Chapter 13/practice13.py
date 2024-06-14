import random

count = 1000000
roulette = random.choices(['red', 'black', 'green'], weights=[18, 18, 2], k=count)

red = (roulette.count('red') / count) * 100
black = (roulette.count('black') / count) * 100
green = (roulette.count('green') / count) * 100



#print('Red percentage is: ' + str(red))
#print('Black percentage is: ' + str(black))
#print('Green percentage is: ' + str(green))
#print('Total percentage is: ' + str(red + black + green))

test_list = [1, 2, 3, 4, 5]
addition = [6, 7, 8]


# test_list.extend(addition)

print(test_list + addition)