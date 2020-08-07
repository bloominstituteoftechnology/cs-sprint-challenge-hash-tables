def get_indices_of_item_weights(weights, length, limit):
    indices = {}

    for i in range(length):
        indices[weights[i]] = i
        target = limit - weights[i]
        print(f"target: {target} = limit: {limit} - weights[i]: {weights[i]}")
        if target in indices:
            if indices[target] > i:
                return (indices[target], i)
            else:
                return (i, indices[target])


    return None

 print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))