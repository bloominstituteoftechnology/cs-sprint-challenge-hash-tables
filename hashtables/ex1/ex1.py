def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_indices = {}

    for i in range(length):
        weight_indices[weights[i]] = i

    for i in range(length):
        our_target = limit - weights[i]
        print(f"The target is: {our_target} - limit: {limit} - weights[i]: {weights[i]}")
        if our_target in weight_indices:
            if weight_indices[our_target] > i:
                return (weight_indices[our_target], i)
            else:
                return (i, weight_indices[our_target])

    return None
