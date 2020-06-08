

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    n_list = len(arrays)
    result = []

    for n in arrays:
        for i in n:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] +=1
                if cache[i] == n_list:
                    result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
