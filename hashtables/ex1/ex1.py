def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
# limit - weight limit
# weights - list of weights

    cache = {}

    # Your code here

# iterate through our list of wights by index
    for i in range(length):
        cache[weights[i]] = i

# iterate list of weights and find matching weights
    for index, weight in enumerate(weights):
        w = limit - weight

        if w in cache:
            i = cache[w]
            return (index, i) if index > i else (i, index)
