def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    
    # loop thru each element in the weights. Use enumerate so we get an index and value for each weight
    for i, num in enumerate(weights):

        # get the difference between the target limit and the current weight
        n = limit - num

        # if the difference isnt in the cache then store the current weight as a key and the index as value
        if n not in cache:
            cache[num] = i
        
        # if the difference is in the cache, this means that there is a key in the cache (an actual weight)
        # that is the difference between the target and the current weight. So we want to return those
        # two indices. 
        else:
            return [max(cache[n], i), min(cache[n], i)]

    return None 
