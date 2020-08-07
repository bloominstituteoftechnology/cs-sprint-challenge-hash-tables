class HashEntry:
    def __init__(self, value, neg):
        self.value = value
        self.neg = neg


def has_negatives(a):
    d = {}
    res = []
    for x in a:
        val = abs(x)
        neg = False if x >= 0 else True
        if val in d:
            if (d[val].neg and not neg) or (not d[val].neg and neg):
                res.append(val)
        else:
            d[val] = HashEntry(val, neg)
    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
