def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    tuple = ()
    # Your code here
    for i, weight in enumerate(weights):
        for l in range(i+1, length):
            if weight + weights[l] == limit: return (l, i)
    return None
