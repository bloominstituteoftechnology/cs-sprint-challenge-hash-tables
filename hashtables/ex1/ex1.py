def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length < 2:
        return None
    for i in range(0, length):
        for j in range(1, length):
            sum = weights[i] + weights[j]
            if sum == limit:
                if weights[i] > weights[j] or weights[j] == 0:
                    if weights[j] == 0:
                        return (j, i)
                    else:
                        return (i, j)
                else:
                    if weights[i] == 0:
                        return (i, j)
                    else:
                        return (j, i)
    return None
