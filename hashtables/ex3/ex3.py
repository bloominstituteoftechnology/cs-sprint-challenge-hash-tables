def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    result = []
    max_val = 0
    for arr in arrays:
        for n in arr:
            if n not in ht:
                ht[n] = 0
            ht[n] = ht[n] + 1
            if ht[n] > max_val:
                max_val = ht[n]
    for n in ht:
        if ht[n] == max_val:
            result.append(n)
    return result

result = intersection([
    [1,2,3],
    [1,4,5,3],
    [1,6,7,3]
])
print(result)
if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
