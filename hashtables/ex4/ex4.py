def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    result = []

    for i in a:
        if i < 0:
            dict[i] = abs(i)
    # print(dict)

    for key, value in dict.items():
        if value in a:
            result.append(value)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
