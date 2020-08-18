def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dict_count = {}

    # ugly nested for loop
    for item in arrays:
        # print(f'  item is {item}')
        for j in item:
            # print(f' j is {j}')
            if j in dict_count: 
                dict_count[j] += 1
            else:
                dict_count[j] = 1    

    # should find [1,3]

    # print(dict_count)
    for item in dict_count.items():
        #  print(f' \t item {item}  item[0]:{item[0]} item[1]:{item[1]}')   # this works !!
        # locate item index when count equals number of arrays iterated
        if item[1] == len(arrays):
            # print(f' key is {item[0]}')
            result.append(item[0])

    # print(result)
    return result

####  REMOVE print statements B4 running tests !!!!!!!!!!!!!
# MVP !!!! ###

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))

# test_arrs = [
#             [1,2,3],
#             [1,4,5,3],
#             [1,3,7,6],

#         ]

# print(intersection(test_arrs))        