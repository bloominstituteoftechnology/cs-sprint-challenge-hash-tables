def get_indices_of_item_weights(weights, length, limit):
    """
    given a list of weights and a limit, returns a pair of those weights which
    sum to the limit.
    """
    
    if length <= 1:
        return None
    else:
        d = {}
        for ind, weight in enumerate(weights):
            d[weight] = ind

        pairs = []
        for ind, weight in enumerate(weights):
            if ((limit - weight) in d) and (d[limit-weight] != ind):
                pairs.append((ind, d[limit-weight]))


        return_pairs = [x if x[0]>x[1] else (x[1],x[0]) for x in pairs]
        #return list(set(return_pairs))[0] # this use of set is purely for removing duplicates.
        return return_pairs[0]

if __name__ == '__main__':
    weights_1 = [9]
    answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
    print(answer_1)

    weights_2 = [4, 4]
    answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
    print(answer_2)

    weights_3 = [4, 6, 10, 15, 16]
    answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
    print(answer_3)

    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
    print(answer_4)