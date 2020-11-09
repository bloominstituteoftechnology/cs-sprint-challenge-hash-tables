def get_indices_of_item_weights(weights, length, limit):
    result_dict = {}

    if len(weights) <= 1:
        return None

    for index, key in enumerate(weights):
        result_dict[key] = index

    for index, key in enumerate(weights):
        difference = limit - key
        if difference in result_dict:
            return (sorted([index, result_dict[difference]], reverse=True))

    return None
