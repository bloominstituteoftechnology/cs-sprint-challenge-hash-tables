def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for index in range(length):
        weight = weights[index]

        if weight in cache:
            value = cache[weight]
            return (index, value)
            
        difference = limit - weight
        cache[difference] = index

    return None
