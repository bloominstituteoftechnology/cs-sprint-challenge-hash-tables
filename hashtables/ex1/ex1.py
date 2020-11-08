def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}

    for index, weight in enumerate(weights):
        hash_table[weight] = index

    for index, weight in enumerate(weights):
        other_weight = limit - weight
        if other_weight in hash_table:
            other_index = hash_table[other_weight]
            if index > other_index:
                return (index, other_index)
            else:
                return (other_index, index)
    return None

if __name__ == "__main__":
    """
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15s and 6 whose sum equals 21
    """
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
