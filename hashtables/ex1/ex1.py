def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = dict()

    for i in range(length):
        # print(weights[i], 'test')
        # weight = weights[i]
        # print(weight)
        if weights[i] in storage:
            previous_weight_index = storage[weights[i]]
            print(previous_weight_index)
            return (i, previous_weight_index)

        storage[limit - weights[i]] = i
        # print(storage)

    return None

# w = [5, 6, 7, 8, 9]
# get_indices_of_item_weights(w, 5, 13)
