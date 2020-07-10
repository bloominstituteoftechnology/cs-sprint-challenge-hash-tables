def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # empty hash table/dictionary
    weight_dict = {}
    # compose each list element as new dictionary key:value pair
    for i in range(len(weights)):
    # as [weight:index] entry
        #check to see if entry already exists
        if weight_dict.get(weights[i]):
        # if so, create a list of values for said key
            weight_dict[weights[i]].append(i)
        # else, procede as usual
        else:
            weight_dict[weights[i]] = [i]
    # iterate through dictionary using length
    
    for weight in weight_dict:
    # subtract the current weight from limit (var)
        add_weight = limit - weight
    # see if dictionary contains that value (var)
        if weight_dict.get(add_weight):
    # if so, return said values, ordered correctly
            # if that key contains a list with > 1 value
            if len(weight_dict[add_weight]) > 1:
            # return those values
                return [weight_dict[add_weight][1], weight_dict[add_weight][0]]
            # else
            weight_sum = [weight_dict[weight][0], weight_dict[add_weight][0]]
            weight_sum.sort(reverse=True)
            return weight_sum 
    # if not, move on to the next item in dictionary
    return None