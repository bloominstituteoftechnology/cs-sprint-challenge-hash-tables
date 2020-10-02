def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}
    arr = []
    for array in arrays:
        arr = arr + array
    for item in arr:
        if item in cache:
            cache[item] += 1
        else:
            cache[item] = 1
    
    # for array in arrays:
    #     for item in array:
    #         if item in cache:
    #             cache[item] += 1
    #         else:
    #             cache[item] = 1
    for key in cache.keys():
        if cache[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
