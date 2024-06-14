import itertools

def avoids(s, l):
    """ takes a string (s) and returns True if it does not contain the forbidden letters (l)
    """
    for letter in s:
        if letter in l:
            return False
    return True


def create_forbidden():
    """ Uses Itertools Combinations to find all possible 5-letter combinations of forbidden characters
        Returns a dictionary where each combination is the key and the value defaults to 0
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    forbidden_five = itertools.combinations(alphabet, 5)
    forbidden_five_dict = {}                             # dictionary that will contain all 65k 5-letter combinations

    for i in forbidden_five:
        delimiter = ''                           # convert the 5-letter combo Tuple into a string sequence
        key = delimiter.join(i)                  # Note: theoretically this isn't required as a dictionary can take a Tuple as a key... but playing it safe for now as not done Tuples yet
        forbidden_five_dict[key] = 0             # Each 5-letter combination becomes a key in the dictionary, with initial value 0 for the counter
    return forbidden_five_dict


def print_forbidden_count():
    fin = open('words.txt')
    count = 0

    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count = count + 1

    print(count)

def delete_later():
    """ Keeping for now as has notes to refer to
    """
    for line in fin:                        # iterate through each word in the word list
        word = line.strip()
        for letters in forbidden_five:      # iterate through all 65k of the possible 5-letter combinations
            if avoids(word, letters):       # if those forbidden letters are avoided...
                pass
                # update the data structure (dictionary?) so that each 5-letter combination has its own counter
                # likely need to create the data structure beforehand, and initilise each counter to 0 for all 65k (key value pair might work here?)
                # could create the dictionary outside this function and intialise with 0 so it's ready to use in the function
                # will come back to this once I've reviewed some of the later chapters again, as it's too much to get my head around at this stage of re-learning
                # another thought I had while going through the Dictionary chapter was that dictionary keys cannot be mutable (e.g. lists)...
                # ... so two ways forward: either 1) wait til I've done Tuples chapter as these are like lists but immutable and so probs can be used as dictionary key,
                # or 2) simply convert each item output from Itertools Combinations function into a string sequence instead. 
                # Could do this in the same for loop that creates the dictionary, then it would be a Key of string sequence and a value of a counter
        print(count)



fin = open('words.txt')
word_list = fin.readlines()
five_combo = create_forbidden() # creates a dictonary with all possible unique 5-letter combinations

progress = 0
end_progress = len(word_list)
initial_progress_interval = 100                 # update to change how fast the progress percentage updates
progress_interval = initial_progress_interval
c = 0

for line in word_list:
        
    word = line.strip().lower()
    
    for forbidden in five_combo:
        if avoids(word, forbidden):
            five_combo[forbidden] += 1

    progress += 1
    if progress == progress_interval:
        progress_percent = (progress / end_progress) * 100
        print('Progress: ' + "{:.2f}".format(progress_percent) + '%', end='\r')
        progress_interval += initial_progress_interval

    
# Note: as of yet I've not run this code to the end as it looks like it'll take a long while (maybe an hour or more) to complete
# Might be worth outputting the final dictionary to a file so it can be played with, as can't really do anything until the comparisons are complete

max_key = max(five_combo, key=five_combo.get)       # returns the key that has the largest value (note: only returns one so could be issues for duplicate values)
print('')
print(max_key)
print(five_combo[max_key])

print(len(word_list))

#print(five_combo)
#print(len(five_combo))