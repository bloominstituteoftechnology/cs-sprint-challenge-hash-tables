def has_negatives(a):
    d = {}
    res = []
    for x in a:
        if abs(x) in d:
            res.append(abs(x))
        else:
            d[abs(x)] = True
    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
