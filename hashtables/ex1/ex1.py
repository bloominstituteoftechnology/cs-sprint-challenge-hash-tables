def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #Needs to return tuple: (zero, one)
    weight_cache = {}
    dupe_weights = {}
    is_dupe = False
    

    for i in range(0, length):
        #creating the weight cache:
        current_weight = weights[i]
        weight_cache[current_weight] = i
        target = limit - current_weight

        if target in weight_cache:
            if current_weight > target or current_weight < target:
                return (i, weight_cache[target])
            elif target == current_weight:
                if is_dupe is False:
                    is_dupe = True
                    dupe_weights[current_weight] = i
                elif is_dupe:
                    return(i, dupe_weights[current_weight])

    return None
