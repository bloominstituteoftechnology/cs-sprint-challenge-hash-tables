def has_negatives(a):
    """
    YOUR CODE HERE
    """

    result = []

    dict = {}

    for num in a:

        dict[num] = num

        if num != 0 and - num in dict:
            result.append(abs(num))
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
