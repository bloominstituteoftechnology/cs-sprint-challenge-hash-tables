def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # $$$
    cache = {}

    # make the keys the weights and the values the indices
    for i in range(len(weights)):
        cache[weights[i]] = i
    # print(cache)
    # for each weight find the difference (complement) and if it matches,
    # return the indices 
    for i in range(len(weights)):
        complement = limit-weights[i]
        if complement in cache:
            return (max(i, cache[complement]), min(i, cache[complement]))
    
    return None
