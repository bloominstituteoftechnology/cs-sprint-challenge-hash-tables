def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    """
    elements have to be sub-arrays
    """
    # Your code here
    d = {}
    result = []
    for el in arrays[0]:
        if el not in d.keys():
            d[el] = 1

    for i in range(1, len(arrays)):
        for el in arrays[i]:
            if el in d.keys():
                d[el] += 1

    for k, v in d.items():
        # did numbers appear in sub-arrays
        if v == len(arrays):
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
