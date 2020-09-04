# FINISHED ###################################################################################
cache = {}
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    for firstArr in arrays[0]:                    # cache the first array
        cache[firstArr] = 1

    for restArr in range(1, len(arrays)):               
        for num in arrays[restArr]:                   # loop through the rest of the arrays
            if num in cache:                           # if the number exist in cache, increase the cache of that num by 1
                cache[num] += 1
                if cache[num] == len(arrays):            # if the value of the cache is equal to length of the array, append to result
                    result.append(num)
    
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    #arrays.append(list(range(1, 20)) + [1, 2, 3])
    #arrays.append(list(range(100, 110)) + [1, 2, 3])
    #arrays.append(list(range(200, 210)) + [1, 2, 3])
    
    print(intersection(arrays))
