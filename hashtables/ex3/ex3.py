def intersection(arrays):
    """
    YOUR CODE HERE
    """
    array_dict = {}
    for each in arrays[0]:
        array_dict[each] = 1
    for i in range(1, len(arrays)):
        for each in arrays[i]:
            if each in array_dict:
                array_dict[each] += 1
    result = []
    for key, value in array_dict.items():
        if value == len(arrays):
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
