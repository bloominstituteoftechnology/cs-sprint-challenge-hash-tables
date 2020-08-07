def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weighttable = {weight: (weight, idx) for idx, weight in enumerate(weights)}
    for i,weight in enumerate(weights):
        if weighttable.get(limit - weight):
            return [max(i, weighttable[limit - weight][1]), min(i, weighttable[limit - weight][1])]

    return None


# print(get_indices_of_item_weights([1,2,3], 3, 3))
# weights_1 = [9]
# answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
# print(answer_1)
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)