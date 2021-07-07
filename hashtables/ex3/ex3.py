def intersection(arrays):
    """
    Objective - find the numbers that exist in all lists
    Input: a list of varying length lists(limit 10) with n integers (limit 1m)
    Output: list of ints/nums that exists in each list in any order
    """
    # initial cache to store computations
    cache = {}

    for arr in arrays:
        for num in arr:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
    
    # initialize empty results list
    results = []
    
    # iterate throgugh cache to get list
    for num, cach in cache.items():
        # if num exists in all the arrays
        if cach == len(arrays):
            results.append(num)
    
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
