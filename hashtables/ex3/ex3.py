def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create dict to hold nums that appear in all lists
    dups_dict = {}
    # loop over each array in the main arr
    for i in arrays: 
    # loop over each item in each inner arr
        for j in i:
            if
    # add all nums in first arr to the dict
    # check if nums in next arr ar in dict, if not, remove from dict.  repeat until no more lists

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
