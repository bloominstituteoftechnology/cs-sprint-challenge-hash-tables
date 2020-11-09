def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    if length <= 1:
        return None
    if length == 2: 
        if sum(weights) == limit: 
            return (1, 0)
        else:
            return None
    else: 
        for idx, weight in enumerate(weights): 
            dict[weight] = idx
        for idx, weight in enumerate(weights):
            if limit-weight in dict:
                if idx < dict[limit-weight]:
                    return (dict[limit-weight],idx)
                else:
                    return (idx, dict[limit-weight])
        return None
                
