test_array = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [
        99,
        2,
        7,
        1,
    ],
]  # expect [1,2]


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = dict()
    arrays.sort(key=len)
    output = []

    for k in arrays[0]:
        table[k] = 1

    i = 1
    while i < len(arrays):
        for k in arrays[i]:
            if table.get(k) is not None:
                table[k] += 1
        i += 1

    for t in table:
        if table[t] == len(arrays):
            output.append(t)

    return output


print(intersection(test_array))

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
