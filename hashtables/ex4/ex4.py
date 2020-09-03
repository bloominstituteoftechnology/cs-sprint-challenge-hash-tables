def has_negatives(a):
    """
    YOUR CODE HERE
    """
    counts = dict()

    for num in a:
        num = abs(num)

        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    result = list()

    for num in counts.items():
        if num[1] == 2:
            result.append(num[0])

    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
