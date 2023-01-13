def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # empty dict
    d = {}
    # for item in a
    for index, value in enumerate(a):
        # add all items to a dict
        d[index] = value
    pos_has_neg = []
    # for key in dict
    for key, value in d.items():
        if value < 0:
            if -value in d:
                pos_has_neg.append(-value)
    return pos_has_neg


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 3, 2, 4, -4]))
