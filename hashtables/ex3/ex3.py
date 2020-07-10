def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    list_dicts = []
    result = []
    index = 0
    for i in range(len(arrays)):
        num_list = arrays[i]
        num_dict = dict(zip(num_list, num_list))
        list_dicts.append(num_dict)
    first = list_dicts.pop(0)
    in_all = None
    for key in first.keys():
        if key in list_dicts[index]:
            in_all = key
            while index is not len(list_dicts) - 1 and in_all is not None:
                index += 1
                if in_all not in list_dicts[index]:
                    in_all = None
                    index = 0
            if in_all is not None:
                result.append(in_all)
            in_all = None
    return result
    
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [5, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 6, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
