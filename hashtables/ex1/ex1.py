def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    table = {weights[x]: [] for x in range(length)}

    for x in range(length):
        for y in table:
            if weights[x] == y:
                table[y].extend([x])

    result = None
    for x in table.keys():
        if limit - x in table.keys():
            if table[x][-1] == table[limit-x][-1]:
                result = (table[x][-1], table[limit-x][-2])
            else:
                result = (table[x][-1], table[limit-x][-1])

    if result:
        return result
    else:
        return None
