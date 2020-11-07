def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    positives = {}

    for i in a:
        if i > 0:
            positives[i] = i
    
    result = [i * -1 for i in a if i * -1 in positives]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
