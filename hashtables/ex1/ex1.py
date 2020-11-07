def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_dict = {}
    tup = []
    # convert list to an dict where key is weight's value 
    # and value is weight's index
    for i, v in enumerate(weights):
            my_dict.update({v:i})
    # check if value minus limit is present in dict
    # if yes, append tuple
    for i, v in enumerate(weights):
        if limit - v in my_dict:
            tup.append(i) 

    # return tuple with larger number in index 0 
    return tup[::-1] or None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))



