def get_indices_of_item_weights(weights, length, limit):
    """
    Return a tuple of integers that stores indices of the elements
    of given weights list if sum of elements is equal to 21
    otherwise return none
    """
    weight_dic ={}
    #travers through the list
    for i in range(len(weights)):
        #store each element(weight) as key in dic
        #and index as value
        if weights[i] not in weight_dic:
            weight_dic[weights[i]] = i
        elif limit - weights[i] ==weights[i]:
            return (i, weight_dic[weights[i]])




    # check if  difference between key and limit 
    # equal to

    for key in weight_dic: 
        if limit - key in weight_dic.keys():    
            key2 = limit - key
            if key2 - key >0:
                return ( weight_dic[key2] , weight_dic[key])
            else:
                return (weight_dic[key2], weight_dic[key])
        
    return None

weights = [ 4, 10, 6, 15, 10]
print(get_indices_of_item_weights(weights, 5, 20))