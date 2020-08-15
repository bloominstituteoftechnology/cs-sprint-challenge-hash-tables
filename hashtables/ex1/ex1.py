def get_indices_of_item_weights(weights, length, limit):
    w_d = {}
    for i in range(0, length):
        if weights[i] in w_d:
            if 2 * weights[i] == limit:
                ind1 = w_d[weights[i]]
                ind2 = i
                output = (ind2, ind1)
                return output
        else:
            w_d[weights[i]] = i
    for x, y in w_d.items():
        e = limit - x
        if e in w_d:
            if w_d[e] > w_d[x]:
                output = (w_d[e], w_d[x])
            elif w_d[x] > w_d[e]:
                output = (w_d[x], w_d[e])
            return output
    return None
