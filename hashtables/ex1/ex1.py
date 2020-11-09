def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # weights = list of each weight,  [ 4, 6, 10, 15, 16 ],
    # length = number of indexs in weights,   5
    # limit = weight total,  21

    cache = {}
    index = 0

    # while index number is less than total lenght of list/array
    while index < length:

        # if (weight total - weights index) not in dictionary
        # 21 - 4 = 17. 17 in weights? No, False
        # 21 - 6 = 15  15 in weights Yes, True!

        if (limit - weights[index]) not in cache:

            cache[weights[index]] = index
            index += 1

        else:
            # return the indexs that add up to 21, which are 1 and 3
            return [index, cache[limit - weights[index]]]
