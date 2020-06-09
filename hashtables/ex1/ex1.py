def get_indices_of_item_weights(weights, length, limit):
    table = {}
    for i in range(len(weights)):
        if weights[i] < limit:
            table[weights[i]] = i
    for i in range(len(weights)):
        try:
            match = limit - weights[i]
            mate = table[match]
            index = i
            thing = [mate, index]
            thing.sort()
            thing.reverse()
            return thing
        except:
            pass
    return None
