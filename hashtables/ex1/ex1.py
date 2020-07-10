def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}
    one = None
    two = None
    if length < 2:
        return None
    for i in range(length):
        if weights[i] not in weight_dict:
            weight_dict.setdefault(weights[i], [i])
        else:
            weight_dict[weights[i]].append(i)
    for i in range(length):
        answer = limit - weights[i]
        if answer in weight_dict:
            if len(weight_dict[answer]) > 1:
                one = weight_dict[answer][0]
                two = weight_dict[answer][1]
            else:
                one = weight_dict[weights[i]][0]
                two = weight_dict[answer][0]
    result = [one, two]
    result.sort(reverse=True)

    return result[0], result[1]

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(f"Answer[0]: {answer_4[0]}, Answer[1]: {answer_4[1]}")