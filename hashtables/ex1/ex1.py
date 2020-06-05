def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight = {}
    duplicates = {}
    duplicates_check = False
    for x in range(0, length):
        current = weights[x]
        weight[current] = x
        target = limit - current
        if target in weight:
            if current > target or current < target:
                return (x, weight[target])
            elif target == current:
                if duplicates_check is False:
                    duplicates_check = True
                    duplicates[current] = x
                elif duplicates_check is True:
                    return (x, duplicates[current])


    return None

"""
line 7: account for duplicate weights [4, 4]
line 8: in order to pass test number 2
line 9: loop through weights and store them into the dictionary 
line 11: setting the value to the index 
line 12: subtracting the current value from the limit to find which package combines to equal weight limit 
line 16: if it finds a duplicate 
"""
# print(get_indices_of_item_weights([4,6,10,15,16], 5, 21))