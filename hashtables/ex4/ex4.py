def has_negatives(a):
    # Why is this slow?
    # dict = {}
    # positives = list(filter(lambda x: x > 0, a))
    # for x in positives:
    #     if -x in a:
    #         dict[x] = True
    #
    # return list(dict.keys())

    dict = {}
    l = []
    for i in a:
        dict[i] = i
        if -i in dict and i != 0:
            l.append(abs(i))
    return l



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
