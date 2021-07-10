def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Define working objects
    ret_arr     = [-999, -999]
    wrk_map     = {}
    flg_found   = False
    lim         = limit

    # Iterate through the inbound weights parameter
    for idx, wgt in enumerate(weights):
        # Add wgt to our map
        if wgt not in wrk_map:
            wrk_map[wgt] = list([idx])
            continue

        wrk_map[wgt].append(idx)

    # Iterate through the inbound list and search for a
    #  a map entry with key = limit - listElement
    for idx, elm in enumerate(weights):
        # Does (limit - listElement) exist in our map as a key?
        tmp_key = lim-elm
        if tmp_key in wrk_map:
            # limit pair exists, save the element and its limit pair
            # to avoid dupes, make sure we're not grabbing the index we're 
            #   currently processing
            tmp_lst = wrk_map[tmp_key]

            # remove the index value that we're currently processing
            if idx in tmp_lst:
                tmp_lst.remove(idx)

            # are there remaining index values?
            if len(tmp_lst) == 0:
                # no more index values, nothing to find, continue processing
                continue 
            
            # have an index value representing a valid weight
            flg_found = True
            # order the returning tuple correctly (high index first)
            if idx > tmp_lst[0]:
                ret_arr[0] = idx
                ret_arr[1] = tmp_lst[0]
                break

            ret_arr[0] = tmp_lst[0]
            ret_arr[1] = idx
            break

    # Did we find an answer?
    if flg_found:
        # Yes
        return tuple(ret_arr)

    # No answer (solution) found
    return None
