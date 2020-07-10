def intersection(arrays):
    """
    Finds the intersection between multiple lists of integers
    """
    # create cache to save the "seen" numbers
    cache = {}

    # get the total number of lists to look through
    num_list = len(arrays)

    # create a list to store the intersection values
    result = []
    
    # loop through each list
    for lst in arrays:
        # loop through each item in that list
        for item in lst:
            # add the item in cache if it's not there (as key)
            # count in how many lists is the item present (as value)
            if item not in cache:
                cache[item] = 1
            else:
                # if the element in already in cash,
                # increment its value by 1
                cache[item] += 1
                # did the item count reach the total number of lists?
                # if yes, add the number in the result list
                if cache[item] == num_list:
                    result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
