def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dictionary = {}

    result = []
    for i in arrays:
        for x in i:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

    for i in dictionary:
        if dictionary[i] >= len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
