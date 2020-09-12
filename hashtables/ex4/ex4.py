def has_negatives(a):
    """
    has_negatives is a function that accepts a list of integers
    and returns positive integers that have a negative "pair"
    
    That is the inbound list include x and -x, then x will be returned
    """
    # Define working variables
    map_pos = {}
    map_neg = {}
    ret_lst = []

    # Iterate through the inbound list value
    for num in a:
        # Place num in the positive or negative map
        if num > 0:
            # Add num to the positive map
            map_pos[num] = None
            continue

        if num < 0:
            # Add num to the negative map
            map_neg[num] = None
            continue

        if num == 0:
            # Ignore '0' as neither positive or negative
            continue

    # Iterate through the postive values (map)
    for key in map_pos.keys():
        # Does -key exist as a dict key in map_neg
        if -key in map_neg:
            # Yes. Add key to our return object
            ret_lst.append(key)

    # Return the the sorted object
    ret_lst.sort()
    return ret_lst

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
