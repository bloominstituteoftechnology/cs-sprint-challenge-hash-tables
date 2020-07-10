def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dict = {}

    for num in a:
        final = num if num > 0 else num * -1
        if final in dict:
            result.append(final)
        else:
            dict[final] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
