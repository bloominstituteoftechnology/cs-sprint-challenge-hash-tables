def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    data = {}

    for x in range(len(weights)):
        data[weights[x]] = x

    for x in range(len(weights)):
        difference = limit - weights[x]
        if difference in data:
            return (max(x, data[difference]), min(x, data[difference]))
