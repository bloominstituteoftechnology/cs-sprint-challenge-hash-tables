def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    for a in arrays:
        for item in a:
            if item not in cache:
                cache[item] = 0
            else:
                cache[item] += 1

    result = []

    for key in cache:
        if cache[key] == len(arrays) - 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
