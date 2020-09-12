from hashtable import HashTable

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = HashTable(16)
    ht_find = HashTable.ht_find
    ht_put = HashTable.ht_put

    if len(weights) == 1:
        return None
    
    for weight in weights:
        ht_put(ht, weight, weights.index(weight))
        if ht_find(ht, (limit - weight)) is not None:
            if weights.index(weight) == ht_find(ht, limit - weight):
                newList = [weights.index(weight)+1, ht_find(ht, limit - weight)]
            else:
                newList = [weights.index(weight), ht_find(ht, limit - weight)]
            
    return newList
