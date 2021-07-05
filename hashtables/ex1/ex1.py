def get_indices_of_item_weights(weights, length, limit):
  
    cache = {}
    result = []

    for index, num in enumerate(weights):
        # define target difference
        target = limit - num

        # look for target in cache
        # if not there add to cache
        if target not in cache:
            cache[num] = index
        # if in cache, append index of each number to result.
        else:
            result.append(index)
            result.append(cache[target])
            return result

    return None

 


