def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    for i in range(len(weights)):
        cache[weights[i]] = i
    for i in range(len(weights)):
        limitWeight = limit - weights[i]
        if limitWeight in cache:
            return (max(i, cache[limitWeight]), min(i, cache[limitWeight]))

