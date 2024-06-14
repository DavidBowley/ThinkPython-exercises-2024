def eval_loop():
    last_exp = ''
    while True:
        user_input = input('Please type your Python expression here and it will be evaluated: ')
        if user_input == 'done':
            break
        last_exp = eval(user_input)
        print(last_exp)
    return last_exp

print(eval_loop())
