def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    storage = {} 
    
    for i, weight in enumerate(weights):        # iterates through each indexed value (weight) in weights
        if limit - weight in storage:    
          return [i, storage[limit - weight]]   # returns the indexed value and the index of the value that when add to it storage in the limit
        storage[weight] = i
    return None


print(get_indices_of_item_weights([40, 80, 50, 70, 60], 5, 100))
