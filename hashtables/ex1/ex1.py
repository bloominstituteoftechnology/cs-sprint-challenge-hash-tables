def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}
    one = None
    two = None
    for i in range(length):
        if weights[i] not in weight_dict:
        # weight_dict[weights[i]] = i
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
                
        # if answer in weight_dict:
        #     if answer is weight_dict[answer]:
        #         return weight_dict[answer][1], weight_dict[answer][0]
        #     else:
        #         return weight_dict[answer], i
    

weights_2 = [4, 4]
answer2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer2)