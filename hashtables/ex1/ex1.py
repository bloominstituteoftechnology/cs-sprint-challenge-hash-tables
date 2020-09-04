# FINISHED ###################################################################################
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for (index, num) in enumerate(weights):
        require = limit - num                             # require = limit - current number
        if require not in cache:                         # if require number is not in cache
            cache[num] = index                           # store the current number in cache with value of index
        else:
            result = []                                   # if require number is in cache
            result.append(index)                         # append the current index
            result.append(cache[require])                # append the require index
            return result                               # return result
    return None
