def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for item in range(length):
        if limit - weights[item] in cache:
            return [item, cache[limit - weights[item]]]
        else:
            cache[weights[item]] = item

    return None
