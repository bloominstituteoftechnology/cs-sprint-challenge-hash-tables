def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    if length <= 1:
        return None

    for i in range(length):
        # start with weight
        weight = weights[i]
        dict[weight] = i
    for n in range(length):
        weight = weights[n]
        difference = limit - weight
        if difference in dict:
            return (dict[difference], n)
    # print(dict)

    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
