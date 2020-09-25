def has_negatives(a):
    """
    YOUR CODE HERE
    """
    ht = {}
    result = []
    for i in a:
        ht[i] = i
        if i != 0 and -i in ht:
            print(i)
            result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
