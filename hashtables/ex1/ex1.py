def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    # Need to loop through the lenght:
        # If limit - weights (in the specific index) in the cache return item and the part
        # Else add the weight at index to cache 
        
    for item in range(length):
        if limit - weights[item] in cache:
            return [item, cache[limit - weights[item]]]
        else:
            cache[weights[item]] = item 

    return None
