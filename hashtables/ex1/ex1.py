def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    limits = {}
    start_index = None
    pair = None
    for i in range(len(weights)):
        # Handle collisions
        if weights[i] in limits:
            limits[weights[i]].append(i)
        else:
            limits[weights[i]] = [i]
        # If the pair is reached return the pair index and the first index
        if weights[i] == pair:
            print('end', i, limit-pair)
            return(i, limits[limit-pair][0])
        # Find a pair and save its value
        if limit - weights[i] in weights:
            pair = limit - weights[i]
            print('start', i, pair)

    return None
