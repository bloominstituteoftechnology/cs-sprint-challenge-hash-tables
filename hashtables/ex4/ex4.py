def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = dict()
    result = []
    a.sort()

    for num in a:
        if num < 0:
            table[-num] = True
        elif num > 0:
            if table.get(num) is True:
                result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))