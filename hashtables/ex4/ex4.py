def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # result = {abs(x): -x for x in a if -x in a}
    pos = {x: 0 for x in a if x > 0}
    neg = {abs(x): 0 for x in a if x < 0}
    result = dict(pos.items() & neg.items())

    return list(result.keys())


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
