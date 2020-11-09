def has_negatives(a):
    """
    YOUR CODE HERE
    """

    result = []

    for number in a:

        if number < 0:
            result.append(abs(number))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
