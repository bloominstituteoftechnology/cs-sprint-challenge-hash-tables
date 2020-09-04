def get_indices_of_item_weights(weights, length, limit):

    weight_index = {k:v for k,v in zip(weights, range(0,len(weights)))}

    for index in range(0,len(weights)):
        # Get current weight
        current_weight = weights[index]
        # Calculate target weight to reach limit 
        target_weight = limit - current_weight
        # If that weight is in the weight_index
        if target_weight in weight_index:
            # if current_weight is greater than target_weight
            if index > weight_index[target_weight]:
                return (index, weight_index[target_weight])
            else:
                return (weight_index[target_weight], index)

    return None
