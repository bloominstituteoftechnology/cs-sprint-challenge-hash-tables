def has_negatives(a):
    # create a dict 
    store = {}
    # create a list to store the values
    result = []
    #iterate over a
    for val in a:
        #if the value is not 0
        if val != 0:
            # the value stored is 1
            store[val] = 1
            #if there are negative values in the store
            if -val in store:
                #append the absolute value to the result
                result.append(abs(val))
    #return the result
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
