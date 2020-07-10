def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight = {}
    dupe_check = False
    duplicates = {}  # in order to pass test 2 we need to account for duplicate values
    # iterate through weights and store them in the dict
    for i in range(0, length):
        # print(weight, dupe_check, duplicates)
        current = weights[i]
        weight[current] = i  # set the value to the index
        # we subtract the current value from the limit to find which package
        # combines to equal weight limit
        target = limit - current
        if target in weight:
            if current > target:
                return (i, weight[target])  # tuple of indexes
            elif current < target:
                return (i, weight[target])
            elif target == current:  # if it finds a dupe
                if dupe_check is False:  # and it isnt already clasified as a duplicate
                    dupe_check = True  # change the bool
                    duplicates[current] = i  # set the value to the index
                elif dupe_check is True:
                    return (i, duplicates[current])
    return None
