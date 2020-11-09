
def get_indices_of_item_weights(weights, length, limit):
    d = {}
    # Your code here
    for index, weight in enumerate(weights):
        if weight in d:
            # what to put here for repeat??
            d[weight] = index
        else:
            d[weight] = index

    # loop through dictionary

    for weight in d:

        if (limit - weight) in d:

            if d[limit-weight] > d[weight]:
                higherIndex = d[limit - weight]
                lowerIndex = d[weight]
            else:
                lowerIndex = d[limit - weight]
                higherIndex = d[weight]

            if higherIndex == lowerIndex:
                lowerIndex = lowerIndex - 1 
            
            return [higherIndex, lowerIndex]


    return None


weights_2 = [4, 4]

print(get_indices_of_item_weights(weights_2, 2, 8))