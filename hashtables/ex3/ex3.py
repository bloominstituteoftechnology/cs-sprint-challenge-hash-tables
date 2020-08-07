import time

def intersection(arrays):
    dict_list = []
    for s in arrays[1:]:
        dicto = {}
        for i in s:
            dicto[i] = True
        dict_list.append(dicto)
    cands = arrays[0].copy()
    result = arrays[0].copy()
    for s in dict_list[1:]:
        for i in cands:
            if i not in s:
                result.remove(i)
        cands = result

    return result


arroz = [
            [1,2],
            [1],
]
print(intersection(arroz))


# start = time.time()

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(100000, 200000)) + [1, 2, 3])
#     arrays.append(list(range(200000, 300000)) + [1, 2, 3])
#     arrays.append(list(range(300000, 400000)) + [1, 2, 3])

#     print(intersection(arrays))
#     print(f'{time.time()-start} seconds')



    # cands = arrays[0].copy()
    # result = arrays[0].copy()
    # for s in arrays[1:]:
    #     for i in cands:
    #         if i not in s:
    #             result.remove(i)
    #     cands = result