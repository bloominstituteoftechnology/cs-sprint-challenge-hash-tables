def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_dict = {}
    for item in a:
        if item < 0:
            num_dict[item] = item

    result = [num for num in a if num * -1 in num_dict]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
