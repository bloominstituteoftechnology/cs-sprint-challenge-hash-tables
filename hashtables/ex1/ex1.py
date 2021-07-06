def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dict = {}

    for i, j in enumerate(weights):

        if limit - j in dict:
            pair = dict.get(limit-j), i
            return tuple(sorted(pair, reverse=True))

        else:
            dict[j] = i

    return None
