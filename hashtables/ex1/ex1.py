cache = {}
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    for i in range(len(weights)):
        cache[weights[i]] = i

    for i, num in enumerate(weights):
        dif = limit - num
        if dif in cache:
            return sorted([i, cache[dif]], reverse=True)

    return None
