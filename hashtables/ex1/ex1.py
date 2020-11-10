def get_indices_of_item_weights(weights, length, limit):

    cache = {}

    for k,v in enumerate(weights): # cache = (4 0, 6 1, 10 2, 15 3, 16 4) key-value pairs 
        cache[v] = k

    for k,w in enumerate(weights): #(0 4, 1 6, 2 10, 3 15, 4 16)
        if (limit-w) in cache:
            if cache[limit-w] > k: # if 3>1
                return (cache[limit-w],k) # (3, 1)
            else:
                return (k, cache[limit-w])
    return None