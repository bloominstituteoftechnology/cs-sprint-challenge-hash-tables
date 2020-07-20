def get_indices_of_item_weights(weights, length, limit):
    # Create a cache
    cache = {}
    # Traverse the weights list in reverse, store the weights as weight: index key:value pair
    for i in reversed(range(len(weights))):
        # Check to see if the the limit - the current value is in the cache
        if limit - weights[i] in cache:
            return [cache[limit - weights[i]], i]
        if weights[i] not in cache:
            # If the the current weight and index are not in the cache add it
            cache[weights[i]] = i

    return None
