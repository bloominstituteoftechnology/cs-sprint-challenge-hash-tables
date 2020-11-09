def intersection(arrays):
    """
    Understand:
    test file ;)

    Plan:
    Create a dict that holds the key as a number in a list.
    The value will be the count of that number in each list.
    Check if the dict value equals number of arrays
    If so the number is in all and should be added to result.

    """

    num_of_arrays = len(arrays)
    count_dict = {}
    result = []

    for lst in arrays:
        for num in lst:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

    for key in count_dict:
        if count_dict[key] == num_of_arrays:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
