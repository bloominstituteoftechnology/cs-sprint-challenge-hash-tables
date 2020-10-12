def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for k, v in enumerate(weights):
        cache[v] = k

    for k, w in enumerate(weights):
        if(limit-w) in cache:
            if cache[limit-w] > k:
                return (cache[limit - w], k)
            else:
                return(k, cache[limit-w])


get_indices_of_item_weights([9], 1, 9)
