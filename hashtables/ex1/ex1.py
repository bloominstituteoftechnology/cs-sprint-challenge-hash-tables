def get_indices_of_item_weights(weights, length, limit):
    # set cache
    cache = {}

    # checks list of weights by index
    for i in range(length):
        cache[weights[i]] = i
   # finds matching weights
    for index, weight in enumerate(weights):
        w = limit - weight
        if w in cache:
            i = cache[w]
            return (index, i ) if index > i else (i, index)
    return None
