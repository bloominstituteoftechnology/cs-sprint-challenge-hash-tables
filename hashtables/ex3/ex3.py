def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # given list of lists that contain integers

    # for i in arrays = each index in arrays [].
    # arrays = [
    # index 0 [1, 2, 3, 4, 5],
    # index 1 [12, 7, 2, 9, 1],
    # index 2 [99, 2, 7, 1,]
    # ]
    # for j in i = need to go deeper to find each i of index
    # index 0 [1, 2, 3, 4, 5]
    # i = [0, 1, 2, 3, 4]

    cache = {}
    result = []

    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1

    for newlist in cache:

        if cache[newlist] == len(arrays):

            result.append(newlist)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


# def intersection(lst1, lst2):
#     lst3 = [value for value in lst1 if value in lst2]
#     return lst3

# # Driver Code
# lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
# lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
# print(intersection(lst1, lst2))
