weights = [4, 6, 10, 15, 16]


# def build_weights_table(weights):

#     for idx, weight in enumerate(weights):

#         if weight not in weight_storage:
#             weight_storage[weight] = idx
#         else:
#             array = list(map(int, str(weight_storage[weight])))
#             print(array)
#             array.append(idx)
#             print(array)
#             weight_storage[weight] = array

#     return weight_storage


def get_indices_of_item_weights(weights, length, limit):

    weight_storage = {}

    for idx in range(length):

        diff = limit - weights[idx]

        if diff in weight_storage:

            pair = weight_storage[diff]

            answer = (idx, pair)
            print(answer)

            return answer

        else:
            weight_storage[weights[idx]] = idx

    # for w in weight_idxs:

    # complements = weight_storage.values()
    # # return sorted(weight_idxs, reverse=True)
    # print(complements)
    # print(sorted(complements))

    # print(weight_idxs)


get_indices_of_item_weights(weights, 5, 21)
