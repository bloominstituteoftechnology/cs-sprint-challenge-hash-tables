def intersection(arrays):
    intersection_dict = {}
    result = []

    # this is going to be used to make sure we have the right number of elements
    num_of_arrays = len(arrays)
    for array in arrays:
        # add elements to dictionary
        for i in array:
            if i not in intersection_dict:
                intersection_dict[i] = 1
            else: 
                intersection_dict[i] += 1

    #iterate through the dictionary and get the items that exist the required times
    for i in intersection_dict:
        if intersection_dict[i] == num_of_arrays:
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
