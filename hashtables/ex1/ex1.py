#weights = [4, 6, 10, 15, 16]

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    hashTable = {} # [weightValue : Index]
    
    for index in range(length):
        weightValue = weights[index]
        target = limit - weightValue
        
        if target not in hashTable:
            hashTable[weightValue] = index
        else: #target in hashTable
            targetIndex = hashTable[target]
            return (index, targetIndex)
            
#get_indices_of_item_weights(weights, 5, 21)


# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
