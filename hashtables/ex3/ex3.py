
def intersection(arr):
    #loop through lists and compare
    #multi = []
    p1 = 1
    same = set(arr[0])
    while p1 <= len(arr)-1:
        same = same & set(arr[p1])
        p1 += 1
        
    return list(same)

    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
