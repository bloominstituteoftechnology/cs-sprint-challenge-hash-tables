def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # assign the weights as dictionary keys and the values as the corrosponding index
    # of those weights
    d = {k: v for k, v in zip(weights, range(length))}

    # with limit - weight find the corrosponding value and build a list of indexes
    for i in d:
        seeking = limit - i

        # edge case
        if seeking == i:
            return [1, 0]

        if seeking in d:
            return [d[seeking], d[i]]

    return None


if __name__ == '__main__':
    a = [4, 4]
    print(get_indices_of_item_weights(a, 2, 8))
