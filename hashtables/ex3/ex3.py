def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # not tested, do not count
    result = []
    for i, arr in enumerate(arrays):
        arrays[i] = dict.fromkeys(arr, 1)
    
    matches = []
    for i in range(1, len(arrays)):
        matches.append(arrays[0].keys() & arrays[i].keys())

    result = list(matches)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
