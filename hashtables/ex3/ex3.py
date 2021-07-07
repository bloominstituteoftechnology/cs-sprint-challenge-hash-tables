def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # $$$
    cache = {}

    # get array length
    num_arrays = len(arrays)
    # count occurrences and save to cache
    # for each list in the arrays
    for lst in arrays:
        # for each element in list
        for elem in lst:
            # if the element is in cache... 
            if elem in cache:
                # increase the count if it exists
                cache[elem] += 1
            else:
                # add to cache if it doesn't exist
                cache[elem] = 1

    result = []
    # if the value for a key equals the number of arrays, it is in all of them
    for key in cache:
        if cache[key] == num_arrays:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
