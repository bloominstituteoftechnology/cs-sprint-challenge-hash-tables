def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    get a dictinary with weights as key and value for index.
    loop thru dic to search the key with limit - current key
    compare the key, return tuple (index higher key, index lower key)

    """
    # Your code here
    cache = {}
    if length == 1:
        return None
    
    if length == 2 and (weights[0] +  weights[1] == limit):
       return 1, 0
    if length == 2 and (weights[0] +  weights[1] != limit):
        return None

    for x in range(length):
        if weights[x] not in cache:
            cache[weights[x]] = x
  

       
    print(cache)  

    for i in range(length):
        if (limit - weights[i]) in cache:
           return cache[limit - weights[i]], i
    return None

if __name__ == "__main__":
    result = get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)
    print(result)