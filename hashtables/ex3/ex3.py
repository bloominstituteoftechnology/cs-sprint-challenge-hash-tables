def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    length = len(arrays)
    result = []
    #loops thru big array of arrays
    for array in arrays:
        #loops thru items in smaller array, if number is not in cache, set number to 1, if number is in cache, increase by 1
        for num in array:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

    #loops thru and checks to see if cached number of items equals the length of the list, appends to result
    for item in list(cache.items()):
        if item[1] == length:
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
