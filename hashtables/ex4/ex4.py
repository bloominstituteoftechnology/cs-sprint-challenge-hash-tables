def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # creat empty dict
    my_dict = {}
    result = []
    # define length and loop over list i
    for num in a:
        #always check if it's in the dictionary FIRST you moron!!!
        if abs(num) not in my_dict:
            my_dict[abs(num)] = num
        else:
            result.append(abs(num))
            print('doooops', result)
    # loop over list j and add to i
      
    # if sum == 0 add to dict

    return result

    has_negatives([-1, -2, 1, 2, 3, 4, -4])


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
