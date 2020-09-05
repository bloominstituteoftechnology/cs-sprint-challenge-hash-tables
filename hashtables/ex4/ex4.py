def has_negatives(lista):
    negs = {}
    possy = {}
    for i in lista:
        if i > 0:
            possy[i] = -i
        else:
            negs[i] = True
    result = []
    for t in possy.items():
        if t[1] in negs:
            result.append(t[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
