def get_indices_of_item_weights(weights, length, limit):
    """
    Finds two items whose sum of weights equals the weight limit.

    Parameters:
    -----------
    weights - list of item weights
    length - length of weights list
    limit - weight limit

    Returns:
    Tuple of integers that has the following form: (zero, one),
        where each element represents the item weights of the two packages.
    The higher valued index in places in the zeroth index
    """
    # create cache
    cache = {}

    # run for each index in the list
    for idx in range(length):
        # weights[idx] is the current weight
        # how much do we need to reach the limit?
        remaining_weight = limit - weights[idx]

        # have we seen already the remaining_weight needed?
        # look in cache
        if remaining_weight in cache:
            # create the result tuple
            result = (idx, cache[remaining_weight])
            # Order descending by weight
            result = sorted(result, reverse=True)
            return result
        else:
            # add the weights in cache
            cache[weights[idx]] = idx

    return None
