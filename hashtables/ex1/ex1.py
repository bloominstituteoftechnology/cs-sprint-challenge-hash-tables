def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(len(weights)):
        w = limit - weights[i]

        if w in cache:
            if cache[w] < i:
                return [i, cache[w]]
            else:
                return [cache[w], i]

        else:
            cache[weights[i]] = i

    return None
