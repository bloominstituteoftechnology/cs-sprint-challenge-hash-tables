def intersection(arrays):
    """
    Params:
    -----
    arrays: of arrays to find intersections

    Returns:
    -----
    results: of items that are found in all lists

    """

    counts = dict()

    # iterate over all items in the lists and add
    # up the count of each item. This is under the 
    # assumption that a number will not be seen more
    # than once in the same list (checked tests)
    for arr in arrays:
        for num in arr:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
    
    results = list()

    # look to see if the value is the same as the
    # number of lists.. if it is, then it should be 
    # seen in all of them
    for k, v in counts.items():
        if v == len(arrays):
            results.append(k)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
