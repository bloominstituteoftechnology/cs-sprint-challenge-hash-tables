weights = [4, 6, 10, 15, 16]


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    ht = {}

    # for i, e in enumerate(weights):
    #     cache[e] = i

    # if cache[e] +
    # return cache

    for i in range(len(weights)):

        # current weight in iteration is the weight at that index
        curr_weight = weights[i]

        # if the current weight is in the cache, that means the other matching weight index is the value in the cache
        if curr_weight in ht:

            # previous/matching weight index is the value
            prev_weight = ht[curr_weight]
            print(ht)

            # i is the larger (current) weight, prev_weight is smaller
            return (i, prev_weight)

        print('current needed weights:', ht)

        # hash table key is the other weight needed to reach limit
        # value is the current weight's index
        ht[limit - curr_weight] = i

    return None


print(get_indices_of_item_weights(weights, 5, 21))
