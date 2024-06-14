def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

def uses_all2(word, required):
    return all(letter in word for letter in required)

def avoids(word, forbidden):
    return set(word) - set(forbidden) == set(word)

def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return res

def binomial_coeff_update(n, k):
    return 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)


print(binomial_coeff_update(5, 2))