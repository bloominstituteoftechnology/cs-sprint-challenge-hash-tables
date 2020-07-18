def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    results = {}

    # for i in range(length):
    #     weight= weights[i]
    #     pair = limit - weight
    #     if pair in results:
    #         return[results[pair], i]
    #     results[weight] = 1
    # return None

    for i, weight in enumerate(weights):
        if limit - weight in results:
          return [results[limit-weight], i]
        results[weight] = i
    return None



print(get_indices_of_item_weights([1,4,8,3,2,9,12,5,6,33], 10, 13))
