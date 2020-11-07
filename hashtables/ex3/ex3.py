from collections import defaultdict

def intersection(arrays):
    hash_table = defaultdict(int)
    result = []
    
    for array in arrays:
        for item in array:
            hash_table[item] += 1
            if hash_table[item] == len(arrays):
                result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
