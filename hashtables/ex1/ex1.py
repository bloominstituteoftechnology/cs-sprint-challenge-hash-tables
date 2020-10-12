def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # cache = {}
    # # keep a count of iterations.
    # weights = enumerate(weights)

    # # x=key : y=value
    # for x, y in weights:
    #     # if y in cache:
    #     if y in cache is True:
    #         # save the value and store the key
    #         cache[y].append(x)
    #     else:
    #         #
    #         cache[y] = x

    # return None

    cache = {}
    length = range(length)
    
    # iterate through lengths list : append to weights 
    for x in length:
        weight = weights[x]

        # if cached weights is true : set value:y to cached weight and return thr key value pair 
        if weight in cache:
            y = cache[weight]
            # return (key, value) pair 
            return (x, y)

        cache[limit - weight] = x


weights = [4, 6, 10, 15, 16]
limit = 21
length = 5
print(get_indices_of_item_weights(weights, length, limit))
