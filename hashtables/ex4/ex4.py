def has_negatives(a):
    neg = {}
    for i in a:
        if i > 0:
            neg[i] = i
    result = [abs(i) for i in a if i * -1 in neg]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
