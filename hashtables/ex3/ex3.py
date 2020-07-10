def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    # dict = {}
    # count = len(arrays)

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

    for item in arrays[0]:
        is_present = True
        for list in arrays:
            if item not in list: is_present = False
        if is_present: result.append(item)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
