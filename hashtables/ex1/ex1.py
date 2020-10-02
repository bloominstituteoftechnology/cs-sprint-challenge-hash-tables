def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {} #Create a cache
    #Create a list of pairs with the remainder of the limit and the indext it took to get there
    possible_combo = [[limit-weight, index] for index, weight in enumerate(weights)]
    for index, weight in enumerate(weights): 
        cache[weight] = index
    for combo in possible_combo: #Run through 1
        if combo[0] in cache:
            return [cache[combo[0]], combo[1]]

    return None
