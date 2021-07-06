def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}

    # loop thru each array
    for i in arrays:

        # for each array loop thru each of the individual components of that array
        for j in i:

            # if the element of the array is in the cache then increase the value of that key by one
            if j in cache:
                cache[j] += 1
            
            # if the element of the array is not in the cache then save the element as a key and set value to 1
            else:
                cache[j] = 1

    # our result is returning each key in the cache if the value of the cache is equal to the length of our list of arrays
    # i.e. if our list of arrays was 3 arrays long, then any key that had a value of 3 means that that key appeared 
    # in all three arrays. 
    result = [k for k, v in cache.items() if v == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
