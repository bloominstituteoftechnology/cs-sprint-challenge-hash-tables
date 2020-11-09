def get_indices_of_item_weights(weights, length, limit):

    cache = {}
    for i in range(length):
        cache[weights[i]] = i
    for i in range(length):
        diff_weight = limit - weights[i]
        if diff_weight in cache.keys():
            pair = sorted((i, cache[diff_weight]), reverse=True)
            return pair
        else:
            continue
    return None

