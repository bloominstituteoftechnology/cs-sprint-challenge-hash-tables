def has_negatives(a):
    """
    find nums in list which have both pos and neg nums in the list
    input: [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
    output: [ 1, 3, 4 ]

    Solution is slow, but it works
    """
    # list for pos and neg numbers
    pos_list = []
    neg_list = []
    # list of lists in order to manipulate values in single cachable object 
    arrays = [pos_list, neg_list]
    
    #initialze hash table/cache
    cache = {}

    # divide lists by pos and neg ints
    for num in a:
        if num > 0:
            pos_list.append(num)
        elif num < 0:
            neg_list.append(abs(num))
    
    # loop thru array in pos and nega arrays to add items to cache
    for arr in arrays:
        for num in arr:
            # if num is in cache, add 1 to count
            if num in cache:
                cache[num] +=1
            # else need to add num to cahce
            else:
                cache[num] = 1

    # initialize empty results list
    results = []
    
    # iterate throgugh cache to get list
    for num, cach in cache.items():
        # if num exists in all the arrays
        if cach == len(arrays):
            results.append(num)
    
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
