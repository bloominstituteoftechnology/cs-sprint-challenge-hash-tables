def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    idx = []
    lookup = {}
    if length > 1:
        for i in range(length):
            lookup[weights[i]] = limit - weights[i]
            if lookup[weights[i]] in weights:
                idx.append(i)
    # print(idx, [weights[idx[0]], weights[idx[1]]])
    if len(idx) > 1:
        if idx[0] > idx[1]:
            return (idx[0], idx[1])
        else:
            return (idx[1], idx[0])

    return None
