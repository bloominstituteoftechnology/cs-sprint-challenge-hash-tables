def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    for arr in arrays:
        for i in arr:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
    # set1 = set(names_1)
    # set2 = set(names_2)
    # names = set1.intersection(set2)
    # duplicates = [name for name in names ]
    result = [x for x in table if table[x]==len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
