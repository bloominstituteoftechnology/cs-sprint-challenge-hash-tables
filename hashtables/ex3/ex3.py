def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    lists = {}
    result = []

    for i in arrays:
        for j in i:
            x = lists.get(j)
            if x is None:
                lists[j] = 1
            else:
                lists[j] = x + 1

    for i in lists.keys():
        value = lists[i]
        if value == len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
