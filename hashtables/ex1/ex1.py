def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    #create my cache dictionary
    cache = {}

    for i in range(length):
        #add the weights value as the "key" in the cache and the index "i" as the value in the cache
        cache[weights[i]] = i

    for i in range(length):
        #value is equal to the limit minus the weights
        #so if the limit 21 minus the weights is equal to a number that is in the cache,
        #then we found 2 items whose sum of weights equals the weight limit
        
        #example: limit: 21 - weight[i]: 4 = 17 (17 is not in cache) so we move on to the next one
        #limit: 21 - weight[i]: 6 = 15 (15 is in cache) so we found our first 2 items whose sum of weights equals the weight limit
        #6 + 15 = 21 (6 is in the cache and 15 is in the cache)
        value = limit - weights[i]
        #print(f"My value: {value}") 

        if value in cache:
            return(max(i, cache[value]), min(i, cache[value]))

    return None

#Example from ReadMe
#input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
#cache: {4: 0, 6: 1, 10: 2, 15: 3, 16: 4}
#output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
