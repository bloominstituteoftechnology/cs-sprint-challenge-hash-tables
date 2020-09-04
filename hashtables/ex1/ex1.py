
cache = {}

def get_indices_of_item_weights(weights, length, limit):
    if length <= 1:
        return None
    if length == 2 and weights[0] + weights[1] == limit:
        return (1,0)
    #make cache of weights : index
    for i in range(length):
        cache[weights[i]] =  i
    
    print(cache)
    # iterate through original weights
    for i in range(length):
        #find weight needed to match limit
        value = limit - weights[i]
        #if find match
        if value in cache:
            item1 = value
            item2 = limit - value
            print(item1, item2)
            if (cache[item1] > cache[item2]):
                return [cache[value], cache[item2]]
            else:
                return [cache[item2], cache[value]]
    return None

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))