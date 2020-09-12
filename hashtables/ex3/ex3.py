def intersection(arrays):
    """
    `intersection` is a function that accepts an array of integer lists
    and returns a list of the integers that are included in every list
    """
    # Working objects/variables
    arr_maps = []
    arr_ret  = []

    # Iterate through the lists of lists
    for lst in arrays:
        # Translate the list to a dict with list values as keys
        tmp_map = dict.fromkeys(lst)

        # Append the map to our array (list) of maps
        arr_maps.append(tmp_map)

    # Done iterating, pop the first map from our array of maps
    iter_map = arr_maps.pop(0)

    # Iterate through the keys of the "popped" map
    for itr_key in iter_map.keys():
        flg_found = True

        # Is this key in every other map?
        #   Iterate through all the other maps and search
        for tmp_map in arr_maps:
            # Is the key being processed in this map?
            if itr_key not in tmp_map:
                # No, break out and continue with the next key
                flg_found = False
                break

        # Was this key found in every map?
        if flg_found:
            # Yes. Add to our return object
            arr_ret.append(itr_key)


    # Done iterating, sort the return list and return the value
    arr_ret.sort()
    return arr_ret

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
