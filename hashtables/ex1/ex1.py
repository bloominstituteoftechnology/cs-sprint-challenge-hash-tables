def get_indices_of_item_weights(weights, length, limit):

    data = {}
    for i in range(len(weights)):
        data[weights[i]] = i
    for i in range(len(weights)):
        dif = limit-weights[i]
        if dif in data:
            return (max(i, data[dif]), min(i, data[dif]))

    return None

#     ans = []
#     if len(weights) < 2:
#         return None
#     for i in range(0, len(weights) - 1):
#         for j in range(1, len(weights) - 1):
#             # print(limit)
#             if (weights[i]+ weights[j]) == limit:
#                 ans.append(i)
#                 ans.append(j)
#             break    
#     return ans
# print(get_indices_of_item_weights([4, 6, 10, 15, 16],5,21))

