def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for i in range(length):
        weight = weights[i]
        complement = limit - weight

        if complement in cache:
            # get index complement from cache
            j = cache[complement]
            # per definition j < i
            return [i,j]
        else:
            # add index weight to cache
            cache[weight] = i

    return None
