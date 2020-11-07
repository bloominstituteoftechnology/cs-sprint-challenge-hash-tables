def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # define hashtable
    my_dict = {}

    # define array to store intersection numbers
    result = []
    # go through arrays of arrays
    for arr in arrays:
        # check every number in current array
        for num in arr:
            # if this number exists already in hashtable, then add it to array
            if num in my_dict:
                result.append(num)
            # if not add to hashtable
            else:
                my_dict[num] = 1
    # extract unique numbers from array converting into dict 
    # and then take only keys by making it a list
    result = list(dict.fromkeys(result))
          
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    # arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(20, 30)) + [1, 2, 3])
    # arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
