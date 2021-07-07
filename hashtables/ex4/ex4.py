def has_negatives(a):
    """
    YOUR CODE HERE
    """
    unique = set(a)
    pos, neg = [i for i in a if i > 0], [j for j in a if j < 0]

    vals = {}
    for i in neg:
        if abs(i) in pos:
            vals.update({abs(i): i})

    result = list(vals.keys())

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
