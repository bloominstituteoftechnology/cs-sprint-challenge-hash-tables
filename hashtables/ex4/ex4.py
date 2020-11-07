def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # define dict
    my_dict = {}
    # go through array to get indeces and values and map them in dict
    for i , v in enumerate(a):
        my_dict.update({i: v})

    # define array 
    result = []
    # go through dict values and find if corresponding negative number exists
    # and add it to result array
    for i in my_dict.values():
        if -i in my_dict and i is not 0:
            result.append(abs(i))
            
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    a = list(range(5000000))
    a += [-1, -2, -3]

    print(has_negatives(a))
