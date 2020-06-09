def intersection(arrays):
    table = {}
    results = []
    for index, values in enumerate(arrays):
        for value in values:
            try:
                table[value] += 1
            except:
                if index == 0:
                    table[value] = 1
    for key in table.keys():
        if table[key] == len(arrays):
            results.append(key)

    return results  
        


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
