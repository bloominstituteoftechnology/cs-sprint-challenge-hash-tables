# For an input list of integers,
# return list of which positive numbers have corresponding negative numbers in the list.
#
# Return value can be in any order.
# Solve this problem with a hash table.

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # empty list
    result = []
    # empty ht
    cache = {}
    
    for num in a:
        # add ints to ht
        cache[num] = 1
    for num in a:
        # if int * -1 is in the ht and positive int exsists, add int to result array
        if (num*-1) in cache and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
