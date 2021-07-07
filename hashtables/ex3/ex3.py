def intersection(arrays):
    """
    YOUR CODE HERE
    """
    element ={}
    #traverse the first list of array
    for row in range(len(arrays)):
        for col in arrays[row]:
           if col not in element:
               element[col]=[row]
           else:
                element[col].append(row)
    
    result=[]
    for key in element.keys():          
        if len(element[key]) == len(arrays):
            result.append(key)
    # for i in arrays[0]:
    #     if i not in element:
    #         element[i] = 0
    # result = []
    # count =0
    # for key in element.keys():
    #     for row in arrays:
    #         if key in row:
    #             count +=1
    #     if count ==len(arrays):
    #        result.append(key)
    
    return result


if __name__ == "__main__":
    arrays = []
 
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
