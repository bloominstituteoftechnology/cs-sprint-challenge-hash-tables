def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}

    for a in arrays:
        for x in a:
            if x in hash_table:
                hash_table[x] += 1
            else:
                hash_table[x] = 1
    
    result = [x[0] for x in hash_table.items() if x[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
