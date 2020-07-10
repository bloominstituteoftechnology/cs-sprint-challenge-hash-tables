def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    intersections = {}
    list_dicts = []
    result = {}
    for i in range(len(arrays)):
        num_dicts = intersections.fromkeys(arrays[i], i)
        list_dicts.append(num_dicts)
    print(num_dicts)
    # for key, value in list_dicts[0].items():
    #     for i in range(len(list_dicts)):
    #         if key in list_dicts[i]:
    #             result[i] = key
    # for list in arrays:
    #     list_count += 1
    #     for num in list:
    #         if list_count is 1 and num not in intersections:
    #             intersections.setdefault(num, [list_count])
    #         if num in intersections:
    #             intersections[num].append(list_count)
    # for key, value in intersections.items():
    #     if value.count is len(arrays):
    #         result.append(key)

    return result
    
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
