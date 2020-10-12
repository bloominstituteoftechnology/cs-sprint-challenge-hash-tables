def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Define working objects and variables
    arr_maps = []
    arr_ret = []

    # Iterate through the lists of lists
    for list in arrays:
        # Convert list into dict w/ list values as keys
        tmp_map = dict.fromkeys(list)

        # Append map to our list of maps
        arr_maps.append(tmp_map)

    # Once finished iterating, pop first map
    iter_map = arr_maps.pop(0)

    # Now, iterate through keys of the popped map
    for itr_key in iter_map.keys():
        fig_found = True

        # Check if key is in other maps
        # Iterate other maps to search
        for tmp_map in arr_maps:
            # Check if key is being processed in this map
            if itr_key not in tmp_map:
                # if no, break loop and continue w/ next key
                fig_found = False
                break

        # Was key found in all maps?
        if fig_found:
            # if yes add to return obj
            arr_ret.append(itr_key)

    # sort return list and values
    arr_ret.sort()
    return arr_ret





if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
