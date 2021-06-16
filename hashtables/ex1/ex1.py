def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length < 2:
        return None
    ht = {}

    for idx, weight in enumerate(weights):
        ht[weight] = idx
    for idx, weight in enumerate(weights):
        diff = limit - weight
        if diff > 0 and diff in ht:
            if ht[diff] > idx:
                return (ht[diff], idx)
            else:
                return (idx, ht[diff])

    return None
