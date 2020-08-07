def intersection(arrays):
  
    cache = {}

    # number of arrays is number of repeats we're looking for
    length = len(arrays)

    result = []

    # look at each array.
    for array in arrays:
        # go through each number.
        for num in array:
            # if number alreay in cache, increase our count.
            if num in cache:
                cache[num] += 1
            # if not add it.
            else:
                cache[num] = 1
    # look through our cache
    for num in cache.items():
        # if value is the same as number of arrays or length
        if num[1] == length:
            # store it
            result.append(num[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
