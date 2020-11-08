def get_indices_of_item_weights(weights, length, limit):
   # create a dictionary with the weight as the key and the index as the value
    cache = {}
    for i in range(length):
        cache[weights[i]] = i

    # we can then loop through the dictionary to see if we have a matching number 
    for index, weight in enumerate(weights):
        w = limit - weight

        if w in cache:
            i = cache[w]
            return (index, i) if index > i else (i, index)

