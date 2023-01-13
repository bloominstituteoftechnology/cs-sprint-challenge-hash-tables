def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}
    for index in range(length):
        bag = []
        cur_weight = weights[index]
        val = hash_table.get(limit-cur_weight)
        if val is None:
            hash_table[cur_weight] = index
        else:
            if val > index:
                bag.append(val)
                bag.append(index)
            else:
                bag.append(index)
                bag.append(val)
            return bag

    return None
