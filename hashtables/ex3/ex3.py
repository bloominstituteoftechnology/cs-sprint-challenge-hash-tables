def intersection(arrays):
    """
    given an arbitrary number of arrays, finds the set intersection
    of the elements of those arrays.
    """
    
    # find out how many arrays we need to intersect
    num_arrays = len(arrays)

    # we'll need to daisy-chain some dicts together
    dict_list = [{} for i in range(num_arrays)]

    # we'll add the elements of the first array to the first dict
    # then for each element of the second array, check if it's in the first dict
    # if it is, we'll add it to the second dict, and then repeat

    # preload the first dictionary
    for element in arrays[0]:
        dict_list[0][element] = element

    # 
    for ii in range(1,num_arrays):
        for element in arrays[ii]:
            if element in dict_list[ii-1]:
                dict_list[ii][element] = element

    # our last dictionary's keys should be the intersecting elements
    result = list(dict_list[-1].keys())


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
