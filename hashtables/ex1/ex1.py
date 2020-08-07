def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    dup_check = False
    dups = {}

    if length <=1:
        print(f"This list is too short to find a complement")
        return None
    
    for i in range(length):
        checking_weight = weights[i]
        cache[checking_weight] = i #add to hashtable

        match_weight = limit - checking_weight
        if match_weight in cache:
            if match_weight == checking_weight:
                if dup_check is False:
                    dup_check = True
                    dups[checking_weight] = i
                else:
                    return (i, dups[checking_weight])
            else:
                return (max(i, cache[match_weight]), min(i, cache[match_weight]))

    return None
