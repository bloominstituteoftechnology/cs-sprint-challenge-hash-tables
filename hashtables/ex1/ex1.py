def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
     # create empty hashtable
    d = {}
    # enumerate weight list
    for index, value in enumerate(weights):
        # if hashtable contains an entry for the weight limit - the current weight value 
        if limit - value in d:
            # get the index of that second value
            pair = d.get(limit-value), index
            return tuple(sorted(pair, reverse=True))
        # if not in hashtable
        else:
            # create entry
            d[value] = index
    return None


weights_2 = [4, 4]

print((get_indices_of_item_weights(weights_2, 2, 8)))
