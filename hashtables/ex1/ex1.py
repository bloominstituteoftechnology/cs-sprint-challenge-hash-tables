def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Fixing PR

    index_dict = {}
    result = []


    # build hashtable with weights
    for i in range(length):
        index_dict[weights[i]] = i

    # print(index_dict)

    # iterate through to find max & min from complement
    for i in range(length):
        current = weights[i]
        complement = limit - current  # could also optimize as >> limit - weights[i]

        if complement in index_dict:
            #print(complement)  
            #result.append(complement)
            # print(i)   
            result.append(i)

    if result:
        # result = sorted(result, reverse = True)
        # return result
        return sorted(result, reverse = True)

    return None   # if nothing found

weights = [9]
print(get_indices_of_item_weights(weights, 1, 9))  # None


weights= [4, 4]
print(get_indices_of_item_weights(weights, 2, 8))   # [1,0]


weights = [ 4, 6, 10, 15, 16 ]  # length = 5, limit = 21
print(get_indices_of_item_weights(weights, len(weights), 21))   # [3,1]