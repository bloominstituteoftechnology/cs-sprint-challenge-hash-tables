def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    Given a box with a max weight 
    ----limit
    A list of weight amounts for each dumbell
    ---- weights
    Number of different weights to box up
    ----length

    Find 2 dumbells whos weight sum equals limit
    If the sum of weights don't equal limit return None

    Create a hashtable then search the table to find sum of 2 weights that == limit
    Store the weight as keys and list index as value

    """
    # Your code here
    table = {}
    diff = limit - weight
    
    for w in range(length):
        




    # return None

# print(get_indices_of_item_weights([4,6,10,15,16], 5, 21))
