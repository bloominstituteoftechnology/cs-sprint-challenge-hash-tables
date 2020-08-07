def get_indices_of_item_weights(weights, length, limit):
    ht = {}

    for i, w in enumerate(weights):
        target = limit - w
    
        if target in ht:
            if ht[target] > i:
                return (ht[target], i)
            else:
                return (i, ht[target])
        else:
            ht[w] = i
    
    return None



get_indices_of_item_weights([ 4, 6, 10, 15, 16 ],5,21)