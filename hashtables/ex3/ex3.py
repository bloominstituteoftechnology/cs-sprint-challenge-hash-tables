def intersection(arrays):

    list_of_lists = arrays

    list_count = len(list_of_lists) # how many lists

    # an element has to show up in every list to be included in response
    tally = {}

    # start with first list
    # tally occurences
    for element in list_of_lists[0]:
        tally[element] = 1

    # for each subsequent list
    for next_list in list_of_lists[1:]:

        # tally occurences
        for new_element in next_list:
        
            # no point in tallying if it has not appeared yet
            if new_element in tally:
                tally[new_element] += 1

    # assumption is that a value occurs zeroce or once per list
    ret_list = [k for (k, v) in tally.items() if v == list_count]

    result = ret_list

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
