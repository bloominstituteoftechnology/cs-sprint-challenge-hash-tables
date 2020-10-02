def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # input(len(arrays))
    table = {}
    result = []
    for array in arrays:
        for entry in array:
            if entry not in table:
                table[entry] = 0
            table[entry] += 1
            if table[entry] == len(arrays):
                result.append(entry)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
