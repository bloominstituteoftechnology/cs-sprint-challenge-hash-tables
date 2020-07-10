def get_indices_of_item_weights(weights, length, limit):
    """
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
    higher value's index goes first
    """
    cache = {}

    for index, val in enumerate(weights):
        cache[limit-val] = index

    print(cache)
    for index, val in enumerate(weights):
        if val in cache:
            index2 = cache[val]
            match = weights[index2]
            if match >= val:
                print(match)
                return [index2,index]
            else:
                print(match)
                return [index,index2]


    return None


print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40],9,7))