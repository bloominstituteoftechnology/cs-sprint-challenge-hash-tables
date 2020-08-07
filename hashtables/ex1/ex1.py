def get_indices_of_item_weights(weights, length, limit):

    #initialize dict to store values
    store = {}

    #set hashtables weights = keys, values = i
    #use emumerate to keep track of iterations w/ key value pairs
    for i, weight in enumerate(weights):
        store [weight] = i
    #iterating through table checking weights that meet limit
    for i, weight in enumerate(weights):
        if limit - weight in store:
            j = store[limit - weight]
            if i > j:
                return (i, j)
            else:
                return(j, i)

    return None
