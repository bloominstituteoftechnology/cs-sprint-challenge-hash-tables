weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # LOOKUP TABLE
    for i in range(len(weights)):
         cache[weights[i]] = i

    for i, num in enumerate(weights):
        dif = limit - num 
        if dif in cache:
            return(sorted([i, cache[dif]], reverse=True))


    return None

print(get_indices_of_item_weights(weights, length, limit))