def get_indices_of_item_weights(weights, length, limit):
    length= len(weights)
    hashmap= dict()

    if length <= 1:
        return None
    for i in range(length):
        weight =weights[i]
        if weight in hashmap:
            value = hashmap[weight]
            return [i, value]
        diff = limit -weight
        hashmap[diff]= i
    return None
