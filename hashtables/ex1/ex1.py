def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weight_index = {}

    for n in range(length):
        weight_index[weights[n]] = n

    for n in range(length):
        tar = limit - weights[n]
        print(f"target: {tar} = limit: {limit} - weights[n]: {weights[n]}")

        if tar in weight_index:
            # Need to sort by large first

            if weight_index[tar] > n:
                return (weight_index[tar], n)
            else:
                return (n, weight_index[tar])

    return None
