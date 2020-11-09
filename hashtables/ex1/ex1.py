def get_indices_of_item_weights(weights, length, limit):
    """
    Understand:
    weights = [12]
    print(get_indices_of_item_weights(weights, 1, 12))  # None


    weights = [4, 3, 1, 5]
    print(get_indices_of_item_weights(weights, 2, 9))   # [3,0]


    weights = [4, 6, 10, 15, 16]  # length = 5, limit = 21
    print(get_indices_of_item_weights(weights, len(weights), 21))   # [3,1]

    Plan:
    Create a dictionary with the weights as values and index as key


    """
    my_dict = {}
    result = []
    if len(weights) >= 1:
        for i, w in enumerate(weights):
            my_dict[w] = i
        # print(my_dict)
    for i in range(length):
        compliment = limit - weights[i]
        if compliment in my_dict:
            result.append(i)
    if result:
        return sorted(result, reverse=True)

    return None


if __name__ == '__main__':
    weights = [4, 6, 10, 15, 16]  # length = 5, limit = 21
    print(get_indices_of_item_weights(weights, len(weights), 21))

    weights = [4, 4]
    print(get_indices_of_item_weights(weights, 2, 8))   # [1,0]
