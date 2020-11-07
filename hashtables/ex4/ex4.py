def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for checking_number in a:
        if checking_number != 0:
            cache[checking_number] = 1  #add to hashtable
            if -checking_number in cache:
                result.append(abs(checking_number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
