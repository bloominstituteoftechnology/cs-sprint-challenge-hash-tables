
d = {}

def get_indices_of_item_weights(weights, length, limit):
    
    for i in range(length):
        d[weights[i]] = weights.index(weights[i])

    for i in range(length):
        if limit - weights[i] in d:
            x = d[limit - weights[i]]

            return (x, d[weights[i]])

# getting 1 failure on test 2