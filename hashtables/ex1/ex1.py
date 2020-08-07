def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    print('something')
    # print inputs to see what they look like
    # needs to return a tuple with 2 integers
    # integers will add up to 'limit'
    # create empty dict
    my_dict = {}
    # loop through array
    print(weights)
    for w in range(length):
        num = limit - weights[w]
        # w is key and num is value
        if num in my_dict:
            # print('weight', my_dict[w])
            print('number', num)
            return w, my_dict[num]
        
        my_dict[weights[w]] = w
        
        print(my_dict[weights[w]])

    return None

get_indices_of_item_weights([2,1,4,3,7,1], 6, 7)
