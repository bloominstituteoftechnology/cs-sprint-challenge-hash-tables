def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    if length < 2:
            return None

    for i in range(length):
        cache[weights[i]] = i

    for index, weight in enumerate(weights):
        target_weight = limit - weight
        
        if target_weight in cache:
            
            target_index = cache[target_weight]
            return (index, target_index) if index > target_index else (target_index, index)
    return None
