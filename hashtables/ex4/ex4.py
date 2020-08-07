def has_negatives(a):

    cache = {}
    result = []

    for num in a:
        # if number not 0 and not in cache add it.
        if num != 0:
            cache[num] = 1
        # if num is in cache, is its opposite in the cache?  If yes, append to results. 
        if -num in cache:
            result.append(abs(num))
            
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
