def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    if length <= 1:
        print("Error: Not enough weights were provided.")
        return None

    for i in range(length):

        weight_remaining = limit - weights[i]

        if weight_remaining in cache:

            weight = cache[weight_remaining]

            weight_limit = (i, weight)

            return weight_limit

        else:

            cache[weights[i]] = i

    return None


# These are the expected test outputs:
print("Test 1", get_indices_of_item_weights(9, 1, 9))
print("Test 2", get_indices_of_item_weights([4, 4], 2, 8))
print("Test 3", get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
print("Test 4", get_indices_of_item_weights(
    [12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
