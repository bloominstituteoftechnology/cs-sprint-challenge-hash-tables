def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # $$$ & result list
    cache = {}
    result = []

    # for number in a...
    for num in a:
        # need to exclude zero
        if num != 0:
            # add number to cache
            cache[num] = 1
            # if number has corresponding positive/negative number
            if -num in cache:
                # add positive num to result via abs
                result.append(abs(num))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
