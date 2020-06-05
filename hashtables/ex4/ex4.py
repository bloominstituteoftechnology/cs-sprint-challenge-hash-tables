def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for num in a:
        # exclude zero
        if num != 0:
            # add num to cache
            cache[num] = 1
            # if num has corresponding positive/negative num
            if -num in cache:
                # add positive num to result
                result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
