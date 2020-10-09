def get_indices_of_item_weights(weights, length, limit):
    combo = {}
    if len(weights) > 1:
        for i in range(0, len(weights)):
            w = weights[i]
            if w in combo:
                val = combo[w]
                return [i, val]
            diff = limit - w
            combo[diff] = i
        return []
    else:
        return None
