def get_indices_of_item_weights(weights, length, limit):
    weight_indices = {}

    for i in range(length):
        weight_indices[weights[i]] = i 
    
    for i in range(length):
        target = limit - weights[i]
        print(f"target: {target} = limit: {limit} - weights[i]: {weights[i]}")
        if target in weight_indices:
            # Need to order by larger index first1
            if weight_indices[target] > i:
                return (weight_indices[target], i)
            else:
                return (i, weight_indices[target])

    return None
