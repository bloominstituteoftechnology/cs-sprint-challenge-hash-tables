def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    hashtable = {}

    # result = [tuple([i, hashtable[limit - weights[i]]])
    #         if (limit - weights[i]) in hashtable
    #         else hashtable[weights[i]] = i
    #         for i in range(length)]
    # return result

    for i in range(length):
        if limit - weights[i] in hashtable:
            result = [i, hashtable[limit - weights[i]]]
            return result
        else:
            hashtable[weights[i]] = i

    return None
