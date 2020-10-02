def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    negatives = {}

    for i in a:
        negatives[i] = -i
    
    result = []

    for i in negatives.keys():
        if i > 0 and negatives[i] in negatives:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
