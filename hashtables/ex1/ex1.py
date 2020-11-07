def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    index = {}

    for i in range(len(weights)):
        # check if hash table contains an entry for limit - weight
        if limit - weights[i] in index:
            # if true, return two items whose weight sum up to the limit
            return [i, index[limit - weights[i]]]
        else:
            index[weights[i]] = i

    return None
