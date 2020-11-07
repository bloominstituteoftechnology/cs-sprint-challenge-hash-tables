def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for index in range(length):
        weight = weights[index]

        if weight in cache:
            value = cache[weight]
            return (index, value)
            
        difference = limit - weight
        cache[difference] = index

    return None

print("Test: ", get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))

