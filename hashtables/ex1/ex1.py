def get_indices_of_item_weights(weights, length, limit):
    
    ht = {} # initialize empty dict 

    for i, v in enumerate(weights):

        # ht contains an entry for weight limit - weight value
        if limit - v in ht:

            # index of second value
            pair = ht.get(limit-v), i
            return tuple(sorted(pair, reverse=True))

        # if not in hashtable, create entry 
        else:

            ht[v] = i

    return None
