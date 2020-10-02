def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for number in a:
        cache[number] = number * -1
    for number in a:
        if (number * -1) in cache:
            if number > 0:
                result.append(number)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
