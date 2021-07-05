def intersection(arrays):
    cache = {}
    # print(arrays)
    result = []
    length = len(arrays)
    counter = 1
    for eachList in arrays:
        for item in eachList:
            if item not in cache:
                cache[item] = counter
            else:
                cache[item] += 1
    for each in cache:
        if cache[each] == length:
            result.append(each)
    return result


if __name__ == "__main__":
    arrays = []

#     # arrays.append(list(range(0, 10)) + [41, 44, 45])
#     # arrays.append(list(range(10, 20)) + [41, 44, 45])
#     # arrays.append(list(range(20, 30)) + [44, 45])

    # arrays.append([1, 2, 3])
    # arrays.append([1,4,5])
    # arrays.append([1,6,7])

    # print(intersection([
    #         [1,2,3],
    #         [1, 3, 4,5],
    #         [1,6,7]
    #     ]))
