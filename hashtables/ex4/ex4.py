# FINISHED ###############################################################################
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negcache = {}
    poscache = {}
    result = []
    for num in a:
        if num not in negcache and num < 0:          # create negative cache
            negcache[num] = num
        elif num not in poscache and num > 0:          # create positive cache
            poscache[num] = num

    for fromPos in poscache:
        if -fromPos in negcache:                        # compare positive cache to negative cache
            result.append(fromPos)                      # append positive number to result if there exists negative number in neg cache

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
