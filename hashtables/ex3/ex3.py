


def intersection(arrays):
    """
    YOUR CODE HERE
    """


    ht = {}
    arr = []
    curr_arr = 1

    #add all values from first array to hashtable as base for quick searching
    for n in arrays[0]:
        ht[n] = n
        # print(ht)

    #while in range of lists
    while curr_arr < len(arrays):
        # print(curr_arr)
        #for number in current list
        for n in arrays[curr_arr]:
            #if that number is in the hashtable--
            if n in ht:
                #--and not in the array
                if n not in arr:
                    #add it to the array
                    arr.append(n)
                curr_arr += 1

    return arr

    # ht = {}

    # for arr in arrays:

    #     for n in arr:

    #         if n in ht:
    #             ht[n] += 1
    #         else:
    #             ht[n] = 1

    # return [nums[0] for nums in ht.items() if nums[1] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
