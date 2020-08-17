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


    """
    # Your code here
    result = []
    table = {}

    for num in a:
        if num < 0:
            num * -1
            print(num)

    # return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
