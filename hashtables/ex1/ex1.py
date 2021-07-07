def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code heres
    cache = {}

    #Edge cases
    
    if length <=1:
        print("Error! Too short")
        return None


    for i in range(length):
        current = weights[i]

        if current in cache:

            previous = cache[current]

            return(i,previous)
    
        cache[limit - weights[i]] = i
    return None


weights = [2, 3, 5, 10, 15]
print(get_indices_of_item_weights(weights, 5, 21))

