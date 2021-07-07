def get_indices_of_item_weights(weights, length, limit):
    """
    This will have an O(weights + 1/2limit) worst case time complexity
    This will have an O(weights) worst case space complexity
    """
    # Your code here
    table = {}

    for i, weight in enumerate(weights):
        if weight in table:
            table[weight].append(i)
        else:
            table[weight] = [i] # list to deal same weight objects

    # limit // 2 - 1 because the minimum value for a lower weight has to be
    # half of the weight limit. - 1 to compensate for range off by one default
    # behavior
    for higher in range(limit, (limit // 2) - 1, -1):
        if higher in table:
            lower = limit - higher
            if lower in table:
                if higher != lower:
                    if table[higher][0] > table[lower][0]: # higher index first
                        return (table[higher][0], table[lower][0])
                    else:
                        return (table[lower][0], table[higher][0])
                elif len(table[higher]) > 1:
                    return (table[higher][1], table[lower][0])

    return None
