def has_negatives(a):
    """
    Params:
    -----
    a: list of both positive and negative integers

    Returns:
    -----
    number if the negative value is also seen in the
    list
    """

    number_dict = dict()
    has_neg = list()

    # iterate over list and check to see if that value * -1
    # is seen in the dictinary.. if so, add it to the list. 
    for number in a:
        if (number * -1) in number_dict:
            has_neg.append(abs(number))
        number_dict[number] = True
    
    # reurn a list with zero repeats
    return list(set(has_neg))


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
