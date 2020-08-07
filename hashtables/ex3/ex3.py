def intersection(arrays):

    counts = dict()

    for arr in arrays:
        for num in arr:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
    
    results = list()

    for k, v in counts.items():
        if v == len(arrays):
            results.append(k)

    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
