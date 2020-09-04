def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_indices = {}

    for i in range(length):
        weight_needed = limit - weights[i]

        if weight_needed in weight_indices:
            j = weight_indices[weight_needed]
            return [i, j]

        weight_indices[weights[i]] = i

    return None
