def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # store all the values from the input to a hash table
    cache = {k: 1 for k in a}

    # create a list from each value in the hash table if the value has a corresponding negative
    # value in the hashtable and the original value is a positive number
    result = [k for k, v in cache.items() if (k*-1) in cache and k > 0]

    

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
