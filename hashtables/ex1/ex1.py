weights = [4, 6, 10, 15, 16]

weight_storage = {}

weight_idxs = []


def build_weights_table(weights):

    for idx, weight in enumerate(weights):

        if weight not in weight_storage:
            weight_storage[weight] = idx
        else:
            array = list(map(int, str(weight_storage[weight])))
            print(array)
            array.append(idx)
            print(array)
            weight_storage[weight] = array

    return weight_storage


def get_indices_of_item_weights(weights, length, limit):

    build_weights_table(weights)

    if length == 1:
        return None

    for weight in weights:

        diff = limit - weight

        if diff not in weight_storage:

            del weight_storage[weight]

        else:
            weight_idxs.append(weight_storage[weight])

    print(weight_idxs)
    print(sorted(weight_idxs, reverse=True))
    # for w in weight_idxs:

    # complements = weight_storage.values()
    # # return sorted(weight_idxs, reverse=True)
    # print(complements)
    # print(sorted(complements))

    return sorted(weight_idxs, reverse=True)

    # print(weight_idxs)


get_indices_of_item_weights(weights, 5, 21)
