def has_negatives(a):
    #initialize empty hash
    d = {}
    # initialize result
    result = []

    # for each value in the passed in list
    for i in a:
        # if the value is greater than 0, it's positive, so add it to the hash
        if i > 0:
            # the value of that hash key is the negative of that value
            d[i] = -i

    # now loop through each hash key in the dictionary
    for i in d:
        # if that hash value is in a
        if d[i] in a:
            # print the hash key
            print(i)


    # this result prints the result for the test case, and it works for the test file
    # but for some reason it gets stuck in an infinite loop
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
