from collections import defaultdict

def intersection(arrays):
    dict = defaultdict(set)

    for list in arrays:
        

    result = []
    # for num in arrays[0]:
    #     for array in arrays:
    #         if num in array:
    #             result.append(num)
                
    set(d[0]).intersection(*d)
    # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
