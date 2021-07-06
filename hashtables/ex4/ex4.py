def has_negatives(a):
    """
    YOUR CODE HERE
    Given a list of nums look for nums that have corresponding negative
    Result can be in any order
    Result is an array

    loop through array 
    make negative numbers pos###### multiply neg num by neg num 
    look for positive nums 
    store in results

    loop through all nums find positive
    store positives in table
    then look for negs and convert to pos
    see if that key is in table if it is then append to result


    """
    # Your code here
    result = []
    table = {}

    for num in a:
        if num > 0:
            if num not in table:
                table[num] = True
                
    for num in a:
        if num < 0:
            num = num * -1
            if num in table:
                result.append(num)

    # for num in a:
    #     if num < 0:
    #         #change num to pos
    #         num = num * -1
    #         # print(num)
    #         if num not in table:
    #             table[num] = 0
    #             if num not in result:
    #                 result.append(num)
    print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 2, 1, 3, 4, -4]))
