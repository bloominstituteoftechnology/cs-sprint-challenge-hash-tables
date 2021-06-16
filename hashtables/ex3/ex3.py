def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    length = len(arrays)
    hash_table = {}
    result = []
    for array in arrays:
        for num in array:
            if not num in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1
    for num, count in hash_table.items():
        if count == length:
            result.append(num)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
