def intersection(arrays):
    # x = range(len(arrays))
    dict_list = []
    for s in arrays:
        dicto = {}
        for i in s:
            dicto[i] = True
        dict_list.append(dicto)
    cands = list(dict_list[0].keys())
    # for s in range(1,len(arrays)):
    #     for i in cands:
    #         if dict_list[s][i]:
    #             continue
    #         cands.pop(i)
    
    return dict_list[1][2] #result

arroz = [
    [1,2,3],
    [1,4,5,3],
    [1,6,7,3]
]

print(intersection(arroz))

'''
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
'''
'''
def intersection(arrays):
    x = range(len(arrays))
    cands = {}
    for i in arrays[0]:
        cands[i] = True
    for s in arrays[1:]:
        for i in s:
            if not cands[i]:

    return cands #result
    '''