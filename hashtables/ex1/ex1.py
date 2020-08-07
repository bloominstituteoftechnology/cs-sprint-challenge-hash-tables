def get_indices_of_item_weights(weights, length, limit):
    """
    Params: 
    ------
    weights: list of item weights
    length: length of list of items
    limit: weight limit
 
    Returns:
    ------
    tuple in form (1, 10)
    where each element represents the item weights of the two packages.
    higher valued index is placed in the `zeroth` index and
    the smaller index is placed in the `first` index. 
    If such a pair doesn’t exist for the given inputs function returns
    `None`.
    """

    weight_dict = dict()

    # enumerate over weights adding each weight to a dictionary
    # for easy lookup latter
    for i, weight in enumerate(weights):

        if weight not in weight_dict:
            weight_dict[weight] = i
        else:
            if weight + weight == limit:
                return (i, weight_dict[weight])
        
    # for each weight, find the difference from the limit to the weight
    # and lookup the difference in the dictionary.. if it's there, return
    # that value
    for weight in weights:
        difference = limit - weight
        if difference in weight_dict:
            return (weight_dict[difference], weight_dict[weight])
    
    # otherwise return None
    return None
