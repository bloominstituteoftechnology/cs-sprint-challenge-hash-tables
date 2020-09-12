def has_negatives(a):
    """
    For an input list of integers, we wish to know which positive numbers have corresponding negative numbers in the list.

Input can be in any order.

Example return value:

[ 1, 3, 4 ]
Because 1, 3, and 4 are the positive numbers that have corresponding negative numbers in the list.

Return value can be in any order.

Solve this problem with a hash table.

Limits:

The input list can contain approximately 5,000,000 elements.
    """
    
    # if abs(i) == i
    dict = {}
    
    # [-1,-2,1,2,3,4,-4] -> [ 1,2,4]
    #  [ 1,2,3] = []
    # [1,2,3,-4] = []
    
    output = []
    for i in a:
        # store greater than 0 elements in dictionary
        if i > 0:
            dict[i] = i
        # if no absolute value of the current number
    for i in a:
        if i * -1 in dict:
            output.append(abs(i))
    return output


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
