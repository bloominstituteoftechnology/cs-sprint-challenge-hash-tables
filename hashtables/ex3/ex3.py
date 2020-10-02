def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # make a cache

    cache = {}
    # we need to loop through every array inside our list of arrays
    for miniarray in arrays:
        # for every number inside the nested array
        for item in miniarray:
            if item not in cache:
                cache[item] = 0
            else:
                cache[item] += 1

    result = []
    # if that index's value is equal to the amount of arrays, it was in all of them.
    # add it to results and return results
    for key in cache:
        if cache[key] == len(arrays) - 1:
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
