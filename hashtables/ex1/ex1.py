def get_indices_of_item_weights(weights, length, limit):

    # initialize the hashtable
    catalog = {}

    # loop over array of weights
    for i in range(len(weights)):

        # set variable that would add up to the limit
        potential_match = limit - weights[i]

        # if potential_match key is in the hashtable, return the indexes
        if potential_match in catalog:
            return (i, catalog[potential_match])

        # otherwise stash the current number we're on in the hash table
        else:
            catalog[weights[i]] = i

    # if there aren't any matches, return None
    return None
