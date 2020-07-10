def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    dictionary = dict()
    
    for i in a:
        dictionary[i] = i
    
    for i in a:
        if i >= 0 and -i in dictionary:
            result.append(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
