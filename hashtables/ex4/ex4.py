def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    tracker = {}
    for num in a:
        if num * -1 in tracker:
            result.append(abs(num))
        tracker[num] = None

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
