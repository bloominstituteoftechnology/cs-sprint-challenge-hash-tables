def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}
    for index, weight in enumerate(weights):
        if limit - weight in weight_dict:
            return [index, weight_dict[limit-weight]]
        weight_dict[weight] = index

    return None
