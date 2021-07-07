def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []

    cache = {}


    for subarray in arrays: 
        for num in subarray: 
            if num not in cache:
                cache[num] = 1
            else: 
                result.append(num)

    result = list(dict.fromkeys(result))


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
