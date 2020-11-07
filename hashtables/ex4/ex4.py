#minus num minus itself

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    my_dict = {}

    for num in a:
        if num < 0:
            my_dict[num] = 0
    
    for num in a:
        #check both
        if num > 0 and num-num *2 in my_dict:
            result.append(num)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
