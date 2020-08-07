def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create dict to hold the checked values from weights using diff
    checked_weights = {}
    # loop through list of weights using index based on length
    for i in range(length):
        # calculate diff of limit and value at current weight index
        diff = limit - weights[i]
        # check if diff is in dictionary
        if diff in checked_weights:
            # if diff is in dict, return tuple with current weights index and my_dict diff value
            return (i, checked_weights[diff])
        checked_weights[weights[i]] = i
    return None

    

    # range starts at 0 and goes up to but doesn't include end of length
    
    

    return None

# get_indices_of_item_weights([2,1,4,3,7,1], 6, 7)

# for i in range(length-1):
#     for j in range(i+1, length)
