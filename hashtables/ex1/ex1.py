def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # First we need to define the objects we'll be working with
    ret_arr = [-999, -999]
    wrk_map = {}
    fig_found = False
    lim = limit

    # Next, iterate through input weights
    for idx, wgt in enumerate(weights):
        # Add wgt to map
        if wgt not in wrk_map:
            wrk_map[wgt] = list([idx])
            continue

        wrk_map[wgt].append(idx)

    # Iterate through the input list
    # Search for map entry where key = limit - listElement
    for idx, elm in enumerate(weights):
        # Check if (limit - listElement) key exists in our map
        tmp_key = lim-elm
        if tmp_key in wrk_map:
            # if limit exists, save to our map
            # check to avoid dupes
            tmp_list = wrk_map[tmp_key]

            # remove index we're currently processing
            if idx in tmp_list:
                tmp_list.remove(idx)

            # check if there are remaining index values
            if len(tmp_list) == 0:
                # if there are no more index values, continue processing
                continue

            # represent weight by index
            fig_found = True

            # order return tuple (largest index goes first)
            if idx > tmp_list[0]:
                ret_arr[0] = idx
                ret_arr[1] = tmp_list[0]
                break

            ret_arr[0] = tmp_list[0]
            ret_arr[1] = idx
            break

    # Check for result
    if fig_found:
        #if yes
        return tuple(ret_arr)

    # if nothing found
    return None


    return None
