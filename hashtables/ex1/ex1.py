def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HER
    """
    cache = {}
    for i in range(length):
        # store weight values as key in cache
        # index location as a value
        cache[weights[i]] = i
    for i in range(length):
        # for each item the val is the limit
        # minus the value of weights[i]
        val = limit - weights[i]
        # if this value exists in the cache
        # we know it equals the limit because
        # together they equal the limit
        '''
        # cache:
        # {4: 0, 6: 1, 10: 2, 15: 3, 16: 4}
        # limit: 21
        # 21 - 4 = 17 (doesn't exist in cache
        # 21-6 = 15 (this number exists in the cache)
        # return the index location of 6, and the value of 15
        '''

        if val in cache:
            # we return the index loc of our original value from length
            # by the key location of our cache at the limit value
            return (max(i, cache[val]), min(i, cache[val]))
    return None