def intersection(arrays):
    store = {}
    for i, lst in enumerate(arrays):
        for num in lst:
            if num not in store:
                if i == 0:
                    store[num] = [str(i)]
                elif num in store and len(store[num]) == i:
                    store[num] += [str(i)]
            else:
                if len(store[num]) == i:
                    store[num] += [str(i)]
    result = []
    for key, value in store.items():
        if len(value) == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
