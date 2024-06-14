def rotate_word(s, n):
    """ Uses caesar encyption to rotate a word by a given number
        s = string to rorate
        n = number to rotate by
    """
    word = s.lower()    # make sure the string is lowercase as ord()/chr() use different numbers for uppercase
    new_word = ''

    for i in word:
        number = ord(i)
        if  number < 97 or number > 122:        # if it's outside of the A to Z range (e.g. a space or other punctuation)
            new_number = number                 # new_number is not actually a rotated number here - just keeps the existing one
        else:                                   # else it is an A to Z letter
            new_number = number + n             # the number code for the current letter plus the rotation number
            if new_number > 122:                # if greater than 122 then needs to wrap around back to 97 (e.g. from Z to A)
                wrap_around = new_number - 122
                new_number = 96 + wrap_around

        new_letter = chr(new_number)            # get the new letter using the number code
        new_word = new_word + new_letter        # keep concatenating each new letter to new_word
    
    return new_word


print(rotate_word("Uv gurer. Guvf vf abg ernyyl wbxr. Whfg univat fbzr sha jvgu gubfr jub pna'g ebg13 na negvpyr. Gb or ernyyl zrna, sbyybj-hc gb guvf negvpyr jvgu fbzrguvat yvxr 'Obl, gung jnf gur shaavrfg wbxr V rire urneq!", 13))