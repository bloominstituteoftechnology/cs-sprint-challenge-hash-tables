def intersection(arrays):
    result = []
    
    for i in range(1, len(arrays)):
        result = [num for num in arrays[0] if num in arrays[i]]

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    arr = [[1,2,3],
            [1,4,5],
            [1,6,7]]
    print(intersection(arr))
