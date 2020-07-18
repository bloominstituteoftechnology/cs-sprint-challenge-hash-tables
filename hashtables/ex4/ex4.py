def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # First instantiate lists for positive and negative numbers
    pos_a = []
    neg_a = []

    # Separate the numbers in a into those lists
    for num in a:
        if num >= 0:
            pos_a.append(num)
        
        else:
            neg_a.append(num)
    
    # Make all values in neg_a positive
    neg_a = [-x for x in neg_a]

    # Instantiate the 'result' list
    result =[]

    # Run a check on every number in pos_a
    for i in pos_a:
        # Only act if i is not already in result
        if i not in result:
            # Append i to result if i is also in neg_a
            if i in neg_a:
                result.append(i)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
