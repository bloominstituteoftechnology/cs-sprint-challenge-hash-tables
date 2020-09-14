def get_indices_of_item_weights(weights, length, limit):
    """
    Items who sum of weights = weight limit
    
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
    """
    cache = {}
        # find target int for each weight in limit
    for i in range(length):
        
        target_weight = limit - weights[i]
        
        # check if weights in the cache
        if target_weight in cache:
            
            # return the selected weight from cache
            tw = cache[target_weight]
            
            # append the item to a new list for each item and cached weight
            output_indices = [i, tw]
            
            # sort the list in reverse ascending order because need zeroeth index to be greater
            output_indices.sort(reverse = True)
            return output_indices
        
        # if target_weight is not in cache then save to cache
        else:
            cache[weights[i]] = i
    return None
