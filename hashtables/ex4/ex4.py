def has_negatives(a):
    """
    given a list of numbers containing negative numbers,
    returns those positive numbers with a corresponding negative element.
    """
    
    # init dict
    d = {}

    # loop over the list once - for each negative value
    # add it's absolute value to the dict

    for element in a:
        if element < 0:
            d[abs(element)] = element

    # loop over a second time - when we find the value
    # in the keys, append to results
     
    result = []
    for element in a:
        if element in d:
            result.append(element)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
