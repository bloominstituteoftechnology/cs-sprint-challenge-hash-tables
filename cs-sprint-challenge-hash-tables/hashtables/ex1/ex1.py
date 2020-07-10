def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dictionary = dict()

    for i in range(length):
        dictionary[weights[i]] = i 

    for i in range(length):
        diff = limit - weights[i]
        if diff in dictionary:
            
            return (max(i,dictionary[diff]), min(i,dictionary[diff]))
            
    return None
