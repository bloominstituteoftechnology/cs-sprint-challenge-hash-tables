def get_indices_of_item_weights(weights, length, limit):
    """
    Given a package with a weight limit limit and a list weights of item
    weights, finds two items whose sum of weights equals the weight limit.

    Returns a tuple of integers where each element represents the item weights
    of the two packages. The higher-valued index is placed in the zeroth index
    and the smaller index is placed in the first index. If such a pair doesn’t
    exist for the given inputs, returns None.

    When multiple solutions exist, only the first found will be returned.
    """

    # Generate a lookup table of indices by weight. O(n).
    lookup = {weight: index for (index, weight) in enumerate(weights)}

    for weight, index in lookup.items():
        # For each item in the list, check to see if there exists a matching
        # counterpart.
        if limit - weight in lookup:
            # If the item under consideration weighs exactly half the limit,
            # check to see if it there is only one such item or whether there
            # are more.
            if limit - weight == weight:
                first = weights.index(weight)
                # If there are multiples, then then the first index will have
                # been overwritten in the process of building the lookup table.
                if first != lookup[weight]:
                    return [lookup[weight], first]
            else:
                # Return the first solution found, if any.
                return sorted([lookup[weight], lookup[limit - weight]],
                              reverse=True)

    # Return None if no solution was found after checking the full table.
    return None
