def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1

            else:
                cache[j] = 1

    result = [i[0] for i in cache.items() if i[1] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
