def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negatives_dict = {}
    result = []

    for num in a:
        negatives_dict[num] = num

        if num != 0 and -num in negatives_dict:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
