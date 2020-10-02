def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    # If we store each weight's list index as its value,
    # we can then check to see if the hash table contains an entry for limit - weight
    # make a cache
    # we're gonna be storing tuples
    # store each weight as a key, value will be that weights index
    # enumerate lets us switch values easily
    cache = {}
    # swithcing the values and storing them in cache
    for k, v in enumerate(weights):
        cache[v] = k

    # find indices of values that sum up to limit value
    for k, w in enumerate(weights):
        # check to see if limit - weight is in cache
        if (limit - w) in cache:
            # if it is, and it is greater than k(being the index of cache), return a tuple
            if cache[limit-w] > k:
                return (cache[limit-w], k)
                # if it is not , flip the order and make k go in front
            else:
                return (k, cache[limit-w])


get_indices_of_item_weights([9], 1, 9)
