weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    create cache
    store weights as keys and index as value
    check if table has entry for limit-weight
    if it does return it
    """
    # Your code here
    cache = {}

    for i in range(len(weights)):
        cache[weights[i]] = i
    for i in range(len(weights)):
        lw = limit - weights[i]
        if lw in cache:
            return ([max(i, cache[lw]), min(i, cache[lw])])

    return None


print(get_indices_of_item_weights(weights, length, limit))