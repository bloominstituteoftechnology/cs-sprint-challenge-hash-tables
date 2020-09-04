def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
        
    # i = 0
    # j = 1
    # gap = 1
    # sums = {}
    # while i < length-1:
    #     while j < length:
    #         key = str(i)+'-'+str(j) if i<=j else str(i)+'-'+str(j)
    #         if key not in sums:
    #             sums[key] = nums[i] + nums[j]  
    #         if(sums[key] == target):
    #             return ([i,j] if i<=j else [j,i])
    #         i += 1
    #         j += 1
    #     gap += 1
    #     j = gap
    #     i = 0 if gap < len(nums) else len(nums)

    
    # for i in range(length):
    #     if limit - weights[i] in weights[i+1:]:
    #         return [i, weights[i+1:].index(limit-weights[i]) + i + 1]

    weights_dict = {}
    dict_to_index = {}
    pos_1 = None
    post_2 = None
    for i,v in enumerate(weights):
        if i not in weights_dict:
            weights_dict[v] = limit - v
            dict_to_index[limit-v] = i

    
    print('weights:       ',weights_dict)
    print('dict to index:', dict_to_index)

    for i,v in enumerate(weights):
        if v in dict_to_index:
            output = [max(i,dict_to_index[v]), min(i,dict_to_index[v])]
            # breakpoint()
            return output
            # return([max(i,dict_to_index[v]),min(i,dict_to_index[v])])



print(get_indices_of_item_weights([4,6,10,15,16],5,21))





