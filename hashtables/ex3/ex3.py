def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # initializing a dict to hold the key value pairs
    dict = {}
    # can be up to 10 lists in all lists
    number_of_lists = len(arrays)
    for each_list in arrays:  # for each of the lists from our input (arrays)
        for each_item in each_list:  # for each item of each list
            if each_item in dict: # if the item is already in the dictionary
                dict[each_item] += 1  # increase the key count
            else:
                dict[each_item] = 1  # add key count of 1 to dict if it isn't already there

    intersections = []
    # we have created a count of how many lists each item exists within
    for key in dict:
        # if it exists in all of them it would be equal to our "number_of_lists"
        if dict[key] == number_of_lists:
            # add the values that intersect to our intersection array
            intersections.append(key)

    return intersections

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))