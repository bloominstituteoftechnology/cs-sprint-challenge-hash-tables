def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    for i in range(length):
        if weights[i] in ht:
            if not isinstance(ht[weights[i]], list):
                ht[weights[i]] = [ht[weights[i]]]
            ht[weights[i]].append(i)
        else:
            ht[weights[i]] = i
    for i, weight in enumerate(weights):
        other_weight = limit - weight
        if other_weight in ht:
            if isinstance(ht[other_weight], list):
                return (ht[other_weight][1], ht[other_weight][0])
            if ht[other_weight] >= ht[weight]:
                return (ht[other_weight], ht[weight])
            else:
                return(ht[weight], ht[other_weight])
    return None

print(get_indices_of_item_weights([4,4], 2, 8))