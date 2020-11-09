def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_dict = {}
    result = []

    for positive in a:
        num_dict[positive] = 1
        if positive != 0 and positive*-1 in num_dict:
           result.append(abs(positive))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
