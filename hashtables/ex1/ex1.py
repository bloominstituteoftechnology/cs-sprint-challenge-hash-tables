def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    lookup = {weight: i for (i, weight) in enumerate(weights)}
    for (i, weight) in enumerate(weights):
        needed_weight = limit - weight
        if needed_weight in lookup:
            return (max(i, lookup[needed_weight]), min(i, lookup[needed_weight]))
    return None

if __name__ == '__main__':
    output = get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
    print(output)
