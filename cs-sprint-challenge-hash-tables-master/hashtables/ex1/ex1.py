def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    if length < 1:
        return None

    cache = {}

    # checking if value in cache
    if limit in cache:
        return cache[limit]

    else:
        # Calculate the entry to the cache
        entry = None

        for index1, weight1 in enumerate(weights):

            cache[weight1] = index1
            
            weight2 = limit - weight1

            if weight2 in weights:
                if weight2 != weight1:
                    index2 = weights.index(weight2)

                else:
                    weights[index1] = weight1 + 1
                    index2 = weights.index(weight2)


                if index1 > index2:
                    entry = (index1, index2)
                    break

                else:
                    entry = (index2, index1)
                    break

        cache[limit] = entry

    return entry