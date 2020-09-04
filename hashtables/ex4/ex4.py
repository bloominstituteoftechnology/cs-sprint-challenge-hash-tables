def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    #loops thru and caches all values into cache
    for x in a:
        cache[x] = x
        #checks to see if negative value of x is in cache
        #append absolute value of x to results
        if -x in cache and x != 0:
            result.append(abs(x))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
