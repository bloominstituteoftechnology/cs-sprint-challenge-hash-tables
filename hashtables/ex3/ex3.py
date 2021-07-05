def intersection(arrays):
    # initialize hash
    d = {}
    #initialize the result
    result = []

    # for all the lists passed in
    # if a number exists in all lists
    # append the number to the result
    # 
    #  
    # another way to say this is
    # if a number exists in ONE listm
    # check if it exists in ALL lists
    # if the number is in all lists, append it to the result



    for i in arrays[0]:
        
            

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
