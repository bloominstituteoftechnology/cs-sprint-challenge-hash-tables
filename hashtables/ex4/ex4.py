def has_negatives(a):
    """
    YOUR CODE HERE
    """
    table = {}
    result = []
    for number in a:
        if number < 0:
            table[number] = True
    for number in a:
        try:
            if table[-number]:
                result.append(number)
        except:
            pass

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
