import pronounce

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

def print_all_homophones(d):
    """ Takes the inverted prounciation dictionary and prints all homophones """
    for pron in d:
        if len(d[pron]) > 1:
            print(d[pron])

def is_homophone(s1, s2, d):
    """ Takes two strings and determines if they are homophones of each other in the dictionary (d) """
    # print(s1, s2)
    # if either string is not a key in the dictionary then it's not a real word and can't be a homophone
    if s1 in d and s2 in d:
        return d[s1] == d[s2]
    else:
        return False

def test_read_dict(d):
    i = 1
    for key in d:
        if i >= 20:
            break
        print(key, d[key])
        i += 1

def first_homophone(d):
    """ Check if there is a homophone between the original word and the word with the first letter removed
        Add to a new dictionary for further testing
        d = dictionary
        Returns a dictionary containing the homophone
    """
    first_rem_homophones = {}
    for word in d:
        if not word[0].isalpha():
            continue
        new_word = word[1:]
        if is_homophone(word, new_word, d):
            first_rem_homophones[word] = new_word
    return first_rem_homophones

def second_homophone(d, orig_d):
    """ Check if there is a homophone between the original word and the word with the second letter removed
        Expects a dictionary where the homophones between the original word and the word with the first letter removed have been found
        d = dictionary with only first homophones
        orig_d = original pronunciation dictionary for checking homophones
    """
    second_rem_homophones = {}
    for word in d: 
        new_word = word[0] + word[2:]
        if is_homophone(word, new_word, orig_d):
            second_rem_homophones[word] = [d[word], new_word]
    return second_rem_homophones

pron_dict = pronounce.read_dictionary()

first_stage = first_homophone(pron_dict)
final_stage = second_homophone(d=first_stage, orig_d=pron_dict)

for word in final_stage:
    print(word, final_stage[word])

