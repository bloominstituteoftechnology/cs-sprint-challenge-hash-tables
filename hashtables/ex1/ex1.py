def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    for i in range(len(weights)):
        if weights[i] not in table:
            table[weights[i]] = i

    if length == 1:
        return None
    elif length == 2 and weights[0] + weights[1] == limit:
        return (1, 0)
    
    for i in range(len(weights)):
        target = limit - weights[i] 
        if target in table:
            val_1 = table.get(target)
            val_2 = i
            if val_2 > val_1:
                return (val_2, val_1)
            return val_1, val_2

weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)