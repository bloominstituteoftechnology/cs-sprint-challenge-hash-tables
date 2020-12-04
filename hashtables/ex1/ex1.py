def get_indices_of_item_weights(weights, length, limit):

    dict = {}
    dict2 = {}

    for w in range(len(weights)):
        weight = {str(weights[w]):w}
        if str(weights[w]) in dict.keys():
            dict2.update(weight)
        else:
            dict.update(weight)
    for i in dict.keys():
        if i in dict2.keys() and limit - int(i) == int(i):
            return [dict2.get(i),dict.get(i)] 
        else:
            continue      
        # weight = {str(w):weights.index(w)}
        # print(weight)
        
        
    print(dict)
    print(dict2)
    # print(list)
    
    for w in dict.keys():
        # print(w)
        x = int(limit) - int(w)
        # print(x)
        if str(x) in dict.keys():
            y = dict.get(str(w))
            z = dict.get(str(x))
            return [z,y]


print(get_indices_of_item_weights([4,4],2, 8))
