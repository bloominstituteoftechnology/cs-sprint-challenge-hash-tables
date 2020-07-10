def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    answer = None
    for item in range(length):
        lookFor = limit - weights[item]
        if lookFor in cache :
            if item <= lookFor:
                answer = (item, cache[lookFor])
            else:
                answer = (cache[lookFor], item)
        else:
            cache[weights[item]] = item
    return answer

