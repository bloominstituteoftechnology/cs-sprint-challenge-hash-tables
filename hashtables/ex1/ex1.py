def get_indices_of_item_weights(weights, length, limit):
    """
    Understand: 
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

    Plan:
   1. create a dict with weights as keys and corresponding indices as values with enumerate. 
    2.now enumerate the weights list 
    3.if (limit-element in weight list) present in dict , compare the value at that key with key for dict 
    creted in step2.
    4.Return the tuple with decending order.

    """
    ht = {}

    for k,v in enumerate(weights): # ht = (4 0, 6 1, 10 2, 15 3, 16 4) key-value pairs 
        ht[v] = k

    for k,w in enumerate(weights): #(0 4, 1 6, 2 10, 3 15, 4 16)
        if (limit-w) in ht:
            if ht[limit-w] > k: # if 3>1
                return (ht[limit-w],k) # (3, 1)
            else:
                return (k, ht[limit-w])
    return None
