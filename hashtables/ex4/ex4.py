def has_negatives(a):
    
    neg = {} # initialize empty dict 

    # loop through (a), add abs val to neg 
    for i in a: 
        if i < 0: 
            neg[abs(i)] = i
    
    result = [] # intialize empty list for results 

    # loop through (a), append to result if val in keys
    for i in a: 
        if i in neg: 
            result.append(i)


    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
