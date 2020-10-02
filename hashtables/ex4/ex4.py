def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # create a cache
    # if number is not in cache, add it
    # we need to compare every single thing in our cache to that value minus itself twice.
    # value = 2, 2 -2 - 2 = -2.
    # now we have a cache with values of 0.
    # loop through array again, for every value in the array, if the opposite version of it is in our cache
    # append it to results

    # check if its opposite, if number is < 0, check if that number + number + number is in our cache,
    # if number > 0 , check if that number - number - number is in our cache
    cache = {}
    for number in a:
        if number not in cache:
            cache[number] = 0
    result = []
    for item in a:
        if item > 0:
            if item-item-item in cache:
                result.append(item)
        elif item < 0:
            if item+item+item in cache:
                result.append(item)
    # need to make a check to we dont have any negative numbers
    for item in result:
        if item < 0:
            result.pop(item)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
