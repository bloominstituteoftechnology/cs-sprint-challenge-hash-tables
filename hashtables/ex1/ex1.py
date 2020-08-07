def get_indices_of_item_weights(weights, length, limit):
    """
    input: weights = [ 4, 6, 10, 15, 16 ],
    length = 5, limit = 21
    output: [ 3, 1 ]  
    # since these are the indices of weights 15 and 6 whose sum equals 21
    """

    # Your code here
    hash_table = {}

    for i in range(length):
        mass = weights[i]
        space = limit - mass

        if space in hash_table:
            x = hash_table[space]
            return[i,x]
            
        else:
            hash_table[mass] = i

    return None
