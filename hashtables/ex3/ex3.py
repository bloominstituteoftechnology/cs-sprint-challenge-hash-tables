def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dict = {}

    for arr in arrays:
        for num in arr:
            if num in dict:
                dict[num] += 1

            else:
                dict[num] = 1

    for d in dict:
        if dict[d] == len(arrays):
            result.append(d)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
