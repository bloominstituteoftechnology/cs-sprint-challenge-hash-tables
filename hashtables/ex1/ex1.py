def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}

    # Start at the end
    curr_index = length - 1

    for i in range(length - 1, 0, -1):
        # Dont use the same index to add
        if i == curr_index:
            continue
        weight = weights[curr_index] + weights[i]
        weight_dict[weight] = (curr_index, i)

    print(weight_dict)

    if limit in weight_dict:
        return weight_dict[limit]

    return None
