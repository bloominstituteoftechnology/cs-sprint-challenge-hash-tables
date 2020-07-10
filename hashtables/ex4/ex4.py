def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    output = []
    for value in a:
        if value != 0:
            cache[value] = 1
            if -value in cache:
                output.append(abs(value))

    return output


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
