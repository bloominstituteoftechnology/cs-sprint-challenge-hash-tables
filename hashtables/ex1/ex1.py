def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    dic = {}
    for i, weight in enumerate(weights):
        try:
            ii = dic[limit - weight]
        except:
            dic[weight] = i
        else:
            return tuple([i, ii])

    return None   

    
