# initialize empty hash
d = {}

def get_indices_of_item_weights(weights, length, limit):
    # create a dictionary with the key being the weight
    # and the value being the index of the weight
    for i in range(length):
        d[weights[i]] = weights.index(weights[i])
    # iterate through the length of the weights list
    for i in range(length):
        # if the difference between the limit and the weight's key exists in the dictionary
        if limit - weights[i] in d:
            # then give that new weight's value a variable name
            x = d[limit - weights[i]]
            # since we know that both exist in the dictionary
            # it's a valid pair of weights that will return 
            return (x, d[weights[i]])

# getting 1 failure on test 2