def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    """ benchmarking against brute force """
    # base_array = arrays[0]

    # for num in base_array:
    #     for array in arrays[1:]:
    #         if num in array:
    #             print(num)

    # for each list in the array
    new_arrays = []
    for i in range(len(arrays)):
    # recreate as a dictionary
        new_arrays.append({})
        for x in range(len(arrays[i])):
            new_arrays[i][arrays[i][x]] = 1
    # iterate through each element in the first dictionary
    for num in new_arrays[0]:
    # check against each subsequent dictionary

        # set variable = 0
        counter = 1
        for array in new_arrays[1:]:
            if array.get(num):
                # if found increment var += 1
                # print(counter)
                counter += 1
                    # if var = len(new_arrays)
                # if it exists in all
                if counter == len(new_arrays):
                    # append to a list
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
