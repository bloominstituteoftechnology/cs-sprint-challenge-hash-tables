def intersection(arrays):

    dicts = []

    for array in arrays:
        dict = {}
        for i in array:
            dict[i] = True
        dicts.append(dict)

    in_all = True
    result = []
    for item in dicts[0].keys():
        #print(dicts[0].keys())
        #print(item)
        for dict in dicts:
            if item in dict:
                pass
                #print(item, "in dictionary so far")
            else:
                # print(item, "not")
                in_all = False

        if in_all == True:
            #print(item, "is officially in dictionary")
            result.append(item)
        else:
            pass
            #print(item, "not in all dictionaries")
        in_all = True

    #print(result)
    return result




if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
