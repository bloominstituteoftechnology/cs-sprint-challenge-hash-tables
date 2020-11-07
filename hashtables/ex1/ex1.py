def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = dict()
    output = []

    for i, w in enumerate(weights):
        table[w] = i

    for weight in table:
        if table.get(limit - weight) is not None:
            output.append(table[weight])

    if output == []:
        return None
    if len(output) == 1:
        output.append(0)
    output.sort(reverse=True)
    # print(table)
    return output


# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))  # expect [3,1]
print(get_indices_of_item_weights([4, 4], 2, 8))  # expect [1,0]
