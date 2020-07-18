def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    results = {}

    for i in range(length):
        weight= weights[i]
        pair = limit - weight
        if pair in results:
            return[results[pair], i]
        results[weight] = 1
    return None

weights = [1,4,8,3,2,9,12]
limit = 13
print(weights)
print(limit)
    
