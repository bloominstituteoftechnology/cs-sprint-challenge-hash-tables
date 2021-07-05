def get_indices_of_item_weights(weights, length, limit, cache={}):
    for index in range(len(weights)):
        cache[weights[index]] = index
    for index in range(len(weights)):
        lw = limit - weights[index]
        if lw in cache:
            return (max(index, cache[lw]), min(index, cache[lw]))
    return None


print(get_indices_of_item_weights([4, 4], 2, 8))
