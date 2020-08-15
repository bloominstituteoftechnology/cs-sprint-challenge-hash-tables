def has_negatives(a):
    int_d = {}
    output = []
    for i in range(len(a)):
        int_d[a[i]] = i
    for x, y in int_d.items():
        if x > 0:
            e = -x
            if e in int_d:
                output.append(x)
    return output
