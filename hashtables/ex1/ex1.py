def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    weights_dict = {}
    dict_to_index = {}
    for i,v in enumerate(weights):
        if i not in weights_dict:
            weights_dict[v] = limit - v
            dict_to_index[limit-v] = i

    for i,v in enumerate(weights):
        if v in dict_to_index:
            output = [max(i,dict_to_index[v]), min(i,dict_to_index[v])]
            return output


# Testing:
print(get_indices_of_item_weights([4,6,10,15,16],5,21))





