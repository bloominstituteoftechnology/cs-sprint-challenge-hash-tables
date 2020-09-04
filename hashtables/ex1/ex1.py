def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    weights_dict = {}
    dict_to_index = {}
    pos_1 = None
    post_2 = None
    for i,v in enumerate(weights):
        if i not in weights_dict:
            weights_dict[v] = limit - v
            dict_to_index[limit-v] = i

    
    # print('weights:       ',weights_dict)
    # print('dict to index:', dict_to_index)

    for i,v in enumerate(weights):
        if v in dict_to_index:
            output = [max(i,dict_to_index[v]), min(i,dict_to_index[v])]
            return output



print(get_indices_of_item_weights([4,6,10,15,16],5,21))





