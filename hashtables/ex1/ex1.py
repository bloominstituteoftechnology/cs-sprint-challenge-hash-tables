def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    for index in range(length):
        # store each weight as a key
        weight = weights[index]
        if weight in cache:
            # you want to store the weight index as the value
            value = cache[weight]
            # return tuple
            return (index, value)
        # calculate the difference
        difference = limit - weight
        # Then, you can add to the cache
        cache[difference] = index

    return None
