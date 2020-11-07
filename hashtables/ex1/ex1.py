def get_indices_of_item_weights(weights, length, limit):
    # CREATE AN EMPTY PYTHON DICTIONARY TO HOLD CACHE
    cache = {}
    # ITERATE OVER THE LIST OF WEIGHTS IN ORDER
    for i in range(len(weights)):
        # CREATE A VARIABLE EQUAL TO THE WEIGHT LIMIT
        # MINUS THE WEIGHT AT THE CURRENT INDEX
        w = limit - weights[i]

        # IF THE VARIABLE WEIGHT IS IN THE CACHE
        if w in cache:
            # AND THE VARIABLE WEIGHT IS LESS THAN THE
            # WEIGHT AT THE CURRENT INDEX
            if cache[w] < i:
                # RETURN THE TWO VALUES IN THIS ORDER
                return [i, cache[w]]
            else:
                # OTHERWISE, RETURN THE TWO VALUES IN
                return [cache[w], i]
        # OTHERWISE, THE CACHE AT INDEX OF WEIGHT AT
        # CURRENT INDEX OF WEIGHT RANGE IS EQUAL TO ITSELF
        else:
            cache[weights[i]] = i

    return None
