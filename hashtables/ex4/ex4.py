def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Define working variables
    map_pos = {}
    map_neg = {}
    ret_list = []

    # iterate through input list
    for num in a:
        # Put num in either pos or neg map
        if num > 0:
            # add num to pos map
            map_pos[num] = None
            continue

        if num < 0:
            # Add num to neg map
            map_neg[num] = None
            continue

        if num == 0:
            # Ignore 0 as neutral
            continue

    # Iterate through pos map
    for key in map_pos.keys():
        # Check if key exist in map_neg
        if -key in map_neg:
            # If yes add key to return obj
            ret_list.append(key)


    # Return the sorted obj
    ret_list.sort()
    return ret_list


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
