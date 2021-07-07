def get_indices_of_item_weights(weights, length, limit):
    
    length = len(weights)
    # Initialize an empty hash table with python dictionary
    hashTable = dict()
    
    if length <= 1:
        return None
    
    # Traverse arr only once. For each weight in arr, compute its complement limit - weight and check wether that complement is hashed so far
    for i in range(length):
        weight = weights[i]
        # If found the complement in the map, return a pair that consists of weight's and limit - weight's indices
        if weight in hashTable:
            value = hashTable[weight]
            return [i, value]
        # If not, hash the weight while using:
        # weight = hash key
        # array index = hash value
        # Even if the same weight is found more than once, it doesn't matter because at the time of the lookup, we only need one item with that weight
        diff = limit - weight
        hashTable[diff] = i
    # if such a pair doesn't exist, return an empty array
    return None

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21
print(get_indices_of_item_weights( weights, length, limit))