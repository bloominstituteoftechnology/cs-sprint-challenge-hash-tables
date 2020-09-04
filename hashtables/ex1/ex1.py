def get_indices_of_item_weights(weights, length, limit):
    """
    desired output: tuple in form (zero, one)
    linear time

    example from README:
    input: weights [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ] # since these are the indices of weights 15 and 6 whose sum equals 21
    """
    # Your code here

    cache = {}

    for i in range(length):

        weight = weights[i]
        pair = limit - weight

        if pair in cache:
            j = cache[pair]
            return [i, j]
        else:
            cache[weight] = i


    return None
