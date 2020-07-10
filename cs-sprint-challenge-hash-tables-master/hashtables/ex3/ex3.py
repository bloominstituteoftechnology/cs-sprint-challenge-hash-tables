def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    main_dict = {}

    # Turn each array into a dictionary
    for index, array in enumerate(arrays):
        dict1 = {}
        for num in array:
            dict1.update({num: None})

        # Add the newly created dictionary to main_dict
        if len(main_dict) == 0:
            main_dict = dict1
        else:
            main_dict = {x:dict1[x] for x in dict1
                            if x in main_dict}

    return list(main_dict) # This should return a list that only has the intersecting values between the lists


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))