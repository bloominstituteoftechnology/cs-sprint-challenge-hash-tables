def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # dict
    cache = {}
    # one array
    single_array = arrays
    # length of arrays
    dicts_length = len(arrays)
    # result 
    result = []

    for single_array in arrays:
        for num in single_array:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1 # make room for it 
            if cache[num] == dicts_length:
                  result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
