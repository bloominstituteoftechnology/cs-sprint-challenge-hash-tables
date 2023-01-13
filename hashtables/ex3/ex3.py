def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # create empty dict
    d = {}
    # put all items in first array into a dict (1,2,3) with value of 1
    for item in arrays[0]:
        # how many times item is in dict
        d[item] = 1
    # for all arrays after the first
    for array in arrays[1:]:
        # for each item in array
        for item in array:
            # if item in dictionary already
            if item in d:
                # increment
                d[item] += 1
            # if not
            else:
                # ignore
                pass
    # create empty intersection list 
    in_every_array = []
    # for each key in our dict
    for key in d:
        # if it is in every array
        if d[key] == len(arrays):
            # append to our intersection list
            in_every_array.append(key)
    # return items where all lists intersect
    return in_every_array


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
