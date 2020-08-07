def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for index in range(length):
        if weights[index] in cache:
            return [index, cache[weights[index]]]
        difference = limit - weights[index]
        cache[difference] = index

    return None