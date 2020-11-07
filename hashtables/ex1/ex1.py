def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    items = {}

    for i in range(length):
        items[weights[i]] = i

    for i in range(length):
        x = limit - weights[i]
        if x in items:
            return(max(i, items[x]), min(i, items[x]))

    return None
