def intersection(arrays):
    """
    YOUR CODE HERE
    """
    count_dict = {}
    num_arrays = 0
    for arr in arrays:
        num_arrays += 1
        for item in arr:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] += 1
    result = [key for key, value in count_dict.items() if value == num_arrays]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
