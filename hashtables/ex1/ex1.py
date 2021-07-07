def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    length = len(weights)
    hashTable = dict()
    
    if length <= 1:
        return None

    for i in range(length):
        weight = weights[i]
        if weight in hashTable:
            value = hashTable[weight]
            return [i, value]
        diff = limit - weight
        hashTable[diff] = i

    return None
