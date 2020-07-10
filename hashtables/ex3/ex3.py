def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    common_int = dict()
    result = []

    for a in arrays:        
        for num in a:
            if num in common_int:
                common_int[0] += 1
            else:
                common_int[0] = 1

            for num in common_int:                
                result = [num for num in common_int]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

    # for i in arrays:
    #     a = arrays[i]
    #     for value in a:
    #         result = [value for value in a if value in a] 
    # return result 
