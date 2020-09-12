def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # will be passed in an array of arrays
    # will cache the first array into the dictionary
    
    cache = {}
    newCache = {}
    for i in range(len(arrays)):
        if i == 0:
            for j in range(len(arrays[i])):
                # doing the caching of the one dictionary
                cache[arrays[i][j]] = ""
        # for the rest will look in the dictionary if the item in the array is not in 
        # the dictionary then the key will be removed from the dictionary
        # by just adding that values that are in their to the newCache
        # and then will rename the cache to what newCache holds
        else: 
            # doing the for loop for the rest of the arrays
            for j in range(len(arrays[i])): 
                if arrays[i][j] in cache:
                    newCache[arrays[i][j]] = ""
            # will now make cache = to newCache
            cache = newCache

    # now making result equal the cache
    result = [*cache]
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
