def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    print('something')
    # print inputs to see what they look like
    # needs to return a tuple with 2 integers
    # integers will add up to 'limit'

    my_dict = {}
    items = weights.sort()
    print(weights)
    (low, high) = (0, leng(items) - 1)

    while low < high:
        if items[low] + items[high] == limit:
            my_dict[0] = (high, low)
            return my_dict
        if items[low] + items[high] < limit:
            low =+ 1
        else: 
            high -= 1 
            



    return None

    get_indices_of_item_weights([2,5,4,3,7,1], 6, 7)
