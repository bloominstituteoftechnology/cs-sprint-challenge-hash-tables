def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for array in arrays:
        for i in array:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 0
    result = [i for i in cache if cache[i]>0]

    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
