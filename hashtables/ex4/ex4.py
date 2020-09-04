def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dictionary = dict()

    result = []

    for i in a:
        dictionary[i] = 1
        if i != 0 and -i in dictionary:
            result.append(abs(i))

    return result
    


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
