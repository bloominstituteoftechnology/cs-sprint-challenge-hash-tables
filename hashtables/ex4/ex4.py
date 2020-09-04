def has_negatives(a):
    # define a hash table where the key is the values in the list and the value
    # for those keys are one
    cache = {k: 1 for k in a}

    # make a list of keys from the cache if the negatives is in the cache and if
    # the value is greater the 0
    result = [k for k, v in cache.items() if (k * -1) in cache and k > 0]

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
