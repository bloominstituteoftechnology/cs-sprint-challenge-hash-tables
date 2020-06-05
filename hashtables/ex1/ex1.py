def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    # base case of insufficient weights
    if length < 2:
            return None

    # case of finding weights
    # create a hashtable of weights and index positions
    for i in range(length):
        cache[weights[i]] = i
    
    # with hashtable complete, let's find potential pairs of weights
    # by assessing each weight's target_weight and checking hashtable for it
    for index, weight in enumerate(weights):
        target_weight = limit - weight # here we compute the target_weight 
        
        if target_weight in cache:
            
            target_index = cache[target_weight] # check if such weight exists
            return (index, target_index) if index > target_index else (target_index, index)
    return None
