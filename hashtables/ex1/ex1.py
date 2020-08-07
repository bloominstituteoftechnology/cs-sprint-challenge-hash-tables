def get_indices_of_item_weights(weights, length, limit):

    # We'll use the zip function to aggregate the iterables in a tuple
    weightIndex = { i:j for i, j in zip(weights, range(0, len(weights)))}

    # We'll use the range function, using 0 as the starting value.
    for index in range(0, len(weights)):
        # We'll get the current weight
        currentWeight = weights[index]
        # Then we'll calculate the target weight by subtracting the the currentweight from the limit
        targetWeight = limit - currentWeight
        # After our calculations, if the target weight is in our weight index
        if targetWeight in weightIndex:
            # if the current weight is greater than the target weight
            if index > weightIndex[targetWeight]:
                return (index, weightIndex[targetWeight])
            else:
                return (weightIndex[targetWeight], index)

    return None
