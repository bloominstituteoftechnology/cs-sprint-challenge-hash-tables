def intersection(arrays):
    result = []
    
    num_count = {}

    # Init arrays
    for i in arrays:
        for k in i:
            if k in num_count:
                num_count[k] += 1
            else:
                num_count[k] = 1
    # Checking to see 
    # Check if appears in all arrays
    for num in num_count:
        if num_count[num] == len(arrays):
            result.append(num)
        else:
            continue

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))