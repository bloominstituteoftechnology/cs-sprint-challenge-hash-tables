def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dicts =[]

    for array in arrays:
        dict = {}
        for i in array:

            dict[i] = True
            
        dicts.append(dict)

    in_all = True
    result =[]
    for item in dicts[0].keys():
        
        for dict in dicts:
            if item in dict:
                pass
            else:
                
                in_all = False
        
        if in_all == True:
            result.append(item)
        else:
            pass

        in_all = True

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
