def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    if len(arrays) == 0:
        return []

    for nums in arrays:
        for num in nums:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1
    return [num for (num, count) in cache.items() if count == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
