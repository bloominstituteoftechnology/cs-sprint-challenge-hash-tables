def intersection(arrays):
    inter = {}
    result = []
    for i in arrays:
        for j in i:
            if j not in inter:
                inter[j] = 1
            else:
                inter[j] += 1
                if inter[j] == len(arrays):
                    result.append(j)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
