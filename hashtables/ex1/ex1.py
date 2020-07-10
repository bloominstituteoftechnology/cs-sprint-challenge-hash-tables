# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`.

def get_indices_of_item_weights(weights, length, limit):
    hashmap = {}
    
    # loop through list
    for i in range(length):
        # store each weight as key
        weight = weights[i]
        # if weight in hashmap
        if weight in hashmap:
            # store weight index as value
            value = hashmap[weight]
            # return tuple with (index, value)
            return (i, value)
        # calc difference
        diff = limit - weight
        # add to hashmap
        hashmap[diff] = i
        
    return None

