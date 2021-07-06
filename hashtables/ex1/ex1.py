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


    for i in range(length):
        # print(w)
        diff = limit - weights[i]

        if diff not in table:
            table[weights[i]] = i
        else:
            diff_weight = table[diff]
            total_limit = (i, diff_weight)
            return total_limit

    return None

print(get_indices_of_item_weights([4,6,10,15,16], 5, 21))
