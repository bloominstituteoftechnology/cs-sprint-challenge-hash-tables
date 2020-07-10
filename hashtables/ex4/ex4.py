def has_negatives(a):
    """
    YOUR CODE HERE
    """
    lookup = {i: -i for i in a if i < 0}
    result = []
    for n in lookup:
        if lookup[n] in a:
            result.append(lookup[n])
    # print(result)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
