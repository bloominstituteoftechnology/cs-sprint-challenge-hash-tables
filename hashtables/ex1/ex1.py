def get_indices_of_item_weights(weights, length, limit):
    # Initialize storage for weights
    dictionary = {}
    # If the input array is less than 2 
    if len(weights) < 2:
        return None
    # Map all weights in a hash table
    for index, weight in enumerate(weights):
        # Check if weight is already in hash table
        if weight in dictionary:
            dictionary[weight].append(index)
        else:
            dictionary[weight] = [index]

    for weight in dictionary:
        diff = limit - weight
         # Check for identical values
        if diff == weight:
            if dictionary[weight][0] > dictionary[weight][1]:
                return (dictionary[weight][0], dictionary[weight][1])
            else:
                return (dictionary[weight][1], dictionary[weight][0])

        # Check the has table for diff
        if diff in dictionary:
            if dictionary[weight][0] > dictionary[diff][0]:
                return (dictionary[weight][0], dictionary[diff][0])
            else:
                return (dictionary[diff][0], dictionary[weight][0])

    return None

        
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)