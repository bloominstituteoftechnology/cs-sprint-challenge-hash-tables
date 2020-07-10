def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # not sure if a set is allowed so using dict...
    negatives = {num: True for num in a if num < 0}
    return [num for num in a if num > 0 and -num in negatives]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
