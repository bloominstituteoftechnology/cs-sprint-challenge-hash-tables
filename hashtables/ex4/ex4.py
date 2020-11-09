def has_negatives(a):
    """
    YOUR CODE HERE
    """
    negatives_set = set(a) # using a set here becasue do not need key value pair
    result = [each for each in a if each > 0 and (0 - each) in negatives_set]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
