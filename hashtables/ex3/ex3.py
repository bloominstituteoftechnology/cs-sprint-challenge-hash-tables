def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    length = len(arrays)

    # count occurrences and save to cache
    for array in arrays:
        for num in array:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1

    # return nums from cache which occur in all arrays
    return [num[0] for num in cache.items() if num[1] is length]



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
