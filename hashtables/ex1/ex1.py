def get_indices_of_item_weights(weights, length, limit):
    if length <=1:
        return None
    elif limit == (weights[0] + weights[1]):
        return (1, 0)
    else:
        weights_lookup = {}

        for x in range(length):
            for y in range(1, length):
                xy_sum = weights[x] + weights[y]
                weights_lookup[xy_sum] = (x, y)

        if limit in weights_lookup:
            return weights_lookup[limit]

    return None