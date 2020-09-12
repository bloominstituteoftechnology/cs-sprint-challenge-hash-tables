def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}
    if len(weights) <= 1:
        return None
  
    for index in range(length):
        current_value = weights[index]

        if current_value in cache:
            cache_index = cache[current_value]
            return (index, cache_index)

        weight_difference = limit - weights[index]    
        cache[weight_difference] = index
 
    return None

weights = [4, 6, 10, 15, 16] 
length = 5 
limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
print(get_indices_of_item_weights(weights, length, limit))