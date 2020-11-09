def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dictionary = {}
    result = []

    for i in a:
        if i == 0:
            continue
        else:
            num = abs(i)
            if num in dictionary:
                dictionary[num] += i
            else:
                dictionary[num] = i

    for i in dictionary:
        if dictionary[i] == 0:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([0, -1, -2, 1, 2, 3, 4, -4]))
