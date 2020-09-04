def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # set up variables
    # result list
    result = []
    # set up hashtable cache
    cache = {}

    # loop through the list
    for num in a:
        # set up num int in cache
        cache[num] = num

        # if number isn't 0 and in cache
        if num != 0 and - num in cache:
            # return number as pos and append
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
