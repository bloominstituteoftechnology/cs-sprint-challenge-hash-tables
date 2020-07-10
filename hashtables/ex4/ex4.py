def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dict = {}

    positives = list(filter(lambda x: x > 0, a))

    for x in a:
        if -x in positives:
            dict[-x] = True

    # Slower
    # for x in a:
    #     for y in a:
    #         if x > 0 and y == -x:
    #             dict[x] = True

    return list(dict.keys())


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
