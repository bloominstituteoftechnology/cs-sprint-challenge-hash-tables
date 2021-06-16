def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # creation of the dictionary to hold the values
    my_cache = {}
    small_index = 0
    larger_index = 0
    # will loop through the list and will put the values in the dictionary
    for i in range(len(weights)):
        
        
            
        if weights[i] not in my_cache:
            my_cache[weights[i]] = i
            if limit - weights[i] == weights[i]:
                continue
        if limit - weights[i] in my_cache:
            # finding out what is the smaller of the two values min = a if a < b else b 
            if i > my_cache[limit - weights[i]]:
                small_index = my_cache[limit - weights[i]]
                larger_index = i
            else:
                small_index = i
                larger_index = my_cache[limit - weights[i]]
            return (larger_index, small_index)
    
    

    return None
