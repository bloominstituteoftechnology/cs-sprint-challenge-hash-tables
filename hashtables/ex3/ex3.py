#ex3.py



def intersection(arrays):

    counts = {}

    for a in arrays:
        for num in a:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

    result = []

    for i, x in counts.items():
        if x == len(arrays):
            result.append(i)

    return result
    

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
