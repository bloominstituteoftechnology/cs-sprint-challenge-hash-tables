def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for l in range(length):
        weight = weights[l]
        complement = limit - weight
        if complement in cache:
            j = cache[complement]
            return [l, j]
        else:
            cache[weight] = l

    return None
