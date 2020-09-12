def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_hash = {}

    for i , w in enumerate(weights):
        smaller_idx = limit - w
        if smaller_idx in weight_hash:
            smaller = weight_hash[smaller_idx]
            return (i, smaller)
        
        weight_hash[w] = i
        
    return None
