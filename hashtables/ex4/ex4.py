# FINISHED ###############################################################################
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negcache = {}
    poscache = {}
    cache = {}
    result = []
    for num in a:
        if -num in cache:                                   # if num has an opposite number of itself in cache
            if num < 0:
                result.append(-num)                        # if num is negative, append the positive version
            else:
                result.append(num)
        else:                                              # if there is not an opposite number, cache the current number
            cache[num] = num                
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
