def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dict = {}
    count = len(arrays)

    # for list in arrays:
    #     hold = []
    #     for item in list:
    #         if item not in hold:
    #             dict[item] = 1 if item not in dict else dict[item] + 1
    #             hold.append(item)
    #
    # for k, v in dict.items():
    #     if v == count: result.append(k)
    # return result

    # for item in arrays[0]:
    #     is_present = True
    #     for list in arrays:
    #         if item not in list: is_present = False
    #     if is_present: result.append(item)

    smallest = len(arrays[0])
    index = 0
    for i, list1 in enumerate(arrays):
        if len(list1) < smallest:
            smallest = len(list1)
            index = i

    for item1 in arrays[index]:
        dict[item1] = 1

    arrays.pop(index)
    for list in arrays:
        for item in list:
            if item in dict:
                dict[item] += 1

    for k, v in dict.items():
        if v == count:
            result.append(k)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
