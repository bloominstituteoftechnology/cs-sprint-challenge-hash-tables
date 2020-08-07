def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}
    for ind, weight in enumerate(weights):
        if weight > limit: #No need to test anything higher than the weight limit
            continue
        inverse = abs(limit - weight)
        if weight in weight_dict.keys(): # We've found a match
            return sorted([ind, weight_dict[weight]], reverse=True)
        else:
            weight_dict[inverse] = ind




    return None
