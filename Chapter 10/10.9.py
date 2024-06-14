def words_to_list(file):
    """ Takes a word list .txt file and builds a list with one word per list item
        .txt file should be formatted with one word per line
        file: location of the file to open (relative to the Python script) 
        Returns the completed list
        Note: this version uses the readlines() method to automatically add to the list
    """
    f = open(file)
    word_list = f.readlines()
    return word_list


def words_to_list_b(file):
    """ Takes a word list .txt file and builds a list with one word per list item
        .txt file should be formatted with one word per line
        file: location of the file to open (relative to the Python script) 
        Returns the completed list
        Note: this version uses the append list method
    """
    f = open(file)
    word_list = []
    for line in f:
        word = line.strip()
        word_list.append(word)
    return word_list


def words_to_list_c(file):
    """ Takes a word list .txt file and builds a list with one word per list item
        .txt file should be formatted with one word per line
        file: location of the file to open (relative to the Python script) 
        Returns the completed list
        Note: this version uses list concatenation and demonstrates how much slower it is to keep creating new lists when you don't need to
    """
    f = open(file)
    word_list = []
    for line in f:
        word = line.strip()
        word_list = word_list + [word]
    return word_list

print(words_to_list_c('words.txt'))