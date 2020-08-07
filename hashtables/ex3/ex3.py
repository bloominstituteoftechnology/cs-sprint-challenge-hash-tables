def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    # Your code here
    result = []
    datatable = {}

    for array in arrays:
        for item in array:
            if item not in datatable:
                datatable[item] = 1
            else:
                datatable[item] += 1
    
    for key, value in datatable.items():
        if value == len(arrays):
            result.append(key)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
