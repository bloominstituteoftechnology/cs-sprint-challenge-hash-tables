def has_negatives(a):
    d = {}
    result = []

    for i in a:
        if i > 0:
            d[i] = -i

    for i in d:
        if d[i] in a:
            print(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
