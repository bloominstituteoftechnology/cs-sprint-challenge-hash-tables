def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}
    for i, weight in enumerate(weights):
        weight_dict[weight] = i

    for i in range(len(weights)):
        value = weights[i]
        complement = limit - value
        if complement in weight_dict:
            if i > weight_dict[complement]:
                return (i, weight_dict[complement])
            else:
                return (weight_dict[complement], i)
    return None


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)